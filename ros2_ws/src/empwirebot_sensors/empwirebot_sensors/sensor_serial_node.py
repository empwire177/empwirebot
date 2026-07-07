#!/usr/bin/env python3

"""
EmpwireBot ROS 2 Sensor Serial Node

Reads ESP32 serial lines like:

SENSOR,F_MM=320,L_MM=450,R_MM=390,B_MM=600,TEMP_C=25.40,HUM_PCT=48.20,MPU_OK=1,AX_G=0.010,AY_G=0.020,AZ_G=1.000,GX_DPS=0.100,GY_DPS=-0.050,GZ_DPS=0.020,ENC_L=120,ENC_R=118,UPTIME_MS=5000

Publishes:
- /distance/front
- /distance/left
- /distance/right
- /distance/back
- /aht10/temperature
- /aht10/humidity
- /encoder/left
- /encoder/right
- /esp32/uptime_ms
- /imu/data
- /odom
"""

import math
from typing import Dict, Optional

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Int64
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry

try:
    import serial
except ImportError:
    serial = None


class SensorSerialNode(Node):
    def __init__(self):
        super().__init__("sensor_serial_node")

        self.declare_parameter("port", "/dev/ttyUSB0")
        self.declare_parameter("baudrate", 115200)
        self.declare_parameter("timer_period", 0.05)

        self.declare_parameter("imu_frame_id", "imu_link")
        self.declare_parameter("odom_frame_id", "odom")
        self.declare_parameter("base_frame_id", "base_link")

        self.declare_parameter("pulses_per_revolution", 20.0)
        self.declare_parameter("wheel_diameter_m", 0.0676)
        self.declare_parameter("wheel_track_width_m", 0.0)
        self.declare_parameter("publish_odom", True)

        self.port = self.get_parameter("port").value
        self.baudrate = int(self.get_parameter("baudrate").value)
        self.timer_period = float(self.get_parameter("timer_period").value)

        self.imu_frame_id = self.get_parameter("imu_frame_id").value
        self.odom_frame_id = self.get_parameter("odom_frame_id").value
        self.base_frame_id = self.get_parameter("base_frame_id").value

        self.pulses_per_revolution = float(self.get_parameter("pulses_per_revolution").value)
        self.wheel_diameter_m = float(self.get_parameter("wheel_diameter_m").value)
        self.wheel_track_width_m = float(self.get_parameter("wheel_track_width_m").value)
        self.publish_odom_enabled = bool(self.get_parameter("publish_odom").value)

        self.distance_per_pulse_m = (
            math.pi * self.wheel_diameter_m / self.pulses_per_revolution
        )

        self.serial_connection = None

        self.previous_left_encoder = None
        self.previous_right_encoder = None
        self.previous_odom_time = None

        self.odom_x = 0.0
        self.odom_y = 0.0
        self.odom_yaw = 0.0

        self.front_pub = self.create_publisher(Float32, "/distance/front", 10)
        self.left_pub = self.create_publisher(Float32, "/distance/left", 10)
        self.right_pub = self.create_publisher(Float32, "/distance/right", 10)
        self.back_pub = self.create_publisher(Float32, "/distance/back", 10)

        self.temperature_pub = self.create_publisher(Float32, "/aht10/temperature", 10)
        self.humidity_pub = self.create_publisher(Float32, "/aht10/humidity", 10)

        self.left_encoder_pub = self.create_publisher(Int64, "/encoder/left", 10)
        self.right_encoder_pub = self.create_publisher(Int64, "/encoder/right", 10)

        self.uptime_pub = self.create_publisher(Int64, "/esp32/uptime_ms", 10)
        self.imu_pub = self.create_publisher(Imu, "/imu/data", 10)
        self.odom_pub = self.create_publisher(Odometry, "/odom", 10)

        self.connect_serial()

        self.timer = self.create_timer(self.timer_period, self.read_serial)

        self.get_logger().info("EmpwireBot Sensor Serial Node Started")
        self.get_logger().info(f"Distance per encoder pulse: {self.distance_per_pulse_m:.5f} m")

        if self.wheel_track_width_m <= 0:
            self.get_logger().warn(
                "wheel_track_width_m is not set. /odom will estimate forward distance only."
            )

    def connect_serial(self):
        if serial is None:
            self.get_logger().error("Python serial module not found. Install python3-serial.")
            return

        try:
            self.serial_connection = serial.Serial(
                self.port,
                self.baudrate,
                timeout=0.01,
            )
            self.get_logger().info(f"Connected to ESP32 on {self.port} at {self.baudrate}")
        except Exception as error:
            self.serial_connection = None
            self.get_logger().error(f"Could not connect to ESP32 on {self.port}: {error}")

    def read_serial(self):
        if self.serial_connection is None:
            return

        try:
            while self.serial_connection.in_waiting > 0:
                raw_line = (
                    self.serial_connection.readline()
                    .decode("utf-8", errors="ignore")
                    .strip()
                )

                if not raw_line:
                    continue

                if not raw_line.startswith("SENSOR,"):
                    continue

                data = self.parse_sensor_line(raw_line)

                if data is None:
                    continue

                self.publish_sensor_data(data)

        except Exception as error:
            self.get_logger().warn(f"Serial read error: {error}")

    def parse_sensor_line(self, line: str) -> Optional[Dict[str, float]]:
        try:
            parts = line.split(",")

            if len(parts) < 2:
                return None

            data = {}

            for part in parts[1:]:
                if "=" not in part:
                    continue

                key, value = part.split("=", 1)
                key = key.strip()
                value = value.strip()

                if key == "":
                    continue

                try:
                    data[key] = float(value)
                except ValueError:
                    self.get_logger().warn(f"Invalid numeric value: {key}={value}")

            return data

        except Exception as error:
            self.get_logger().warn(f"Parse error: {error}")
            return None

    def publish_float_if_valid_mm(self, data: Dict[str, float], key: str, publisher):
        if key not in data:
            return

        value_mm = data[key]

        if value_mm < 0:
            return

        value_m = value_mm / 1000.0

        msg = Float32()
        msg.data = float(value_m)
        publisher.publish(msg)

    def publish_float_if_valid(
        self,
        data: Dict[str, float],
        key: str,
        publisher,
        invalid_value: float = -999.0,
    ):
        if key not in data:
            return

        value = data[key]

        if math.isclose(value, invalid_value, abs_tol=0.01):
            return

        msg = Float32()
        msg.data = float(value)
        publisher.publish(msg)

    def publish_int_if_valid(self, data: Dict[str, float], key: str, publisher):
        if key not in data:
            return

        msg = Int64()
        msg.data = int(data[key])
        publisher.publish(msg)

    def publish_imu_if_valid(self, data: Dict[str, float]):
        required_keys = [
            "MPU_OK",
            "AX_G",
            "AY_G",
            "AZ_G",
            "GX_DPS",
            "GY_DPS",
            "GZ_DPS",
        ]

        for key in required_keys:
            if key not in data:
                return

        if int(data["MPU_OK"]) != 1:
            return

        g_to_mps2 = 9.80665
        dps_to_radps = math.pi / 180.0

        msg = Imu()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.imu_frame_id

        msg.orientation_covariance[0] = -1.0

        msg.linear_acceleration.x = float(data["AX_G"] * g_to_mps2)
        msg.linear_acceleration.y = float(data["AY_G"] * g_to_mps2)
        msg.linear_acceleration.z = float(data["AZ_G"] * g_to_mps2)

        msg.angular_velocity.x = float(data["GX_DPS"] * dps_to_radps)
        msg.angular_velocity.y = float(data["GY_DPS"] * dps_to_radps)
        msg.angular_velocity.z = float(data["GZ_DPS"] * dps_to_radps)

        msg.angular_velocity_covariance[0] = 0.01
        msg.angular_velocity_covariance[4] = 0.01
        msg.angular_velocity_covariance[8] = 0.01

        msg.linear_acceleration_covariance[0] = 0.1
        msg.linear_acceleration_covariance[4] = 0.1
        msg.linear_acceleration_covariance[8] = 0.1

        self.imu_pub.publish(msg)

    def yaw_to_quaternion(self, yaw: float):
        half_yaw = yaw * 0.5
        return {
            "x": 0.0,
            "y": 0.0,
            "z": math.sin(half_yaw),
            "w": math.cos(half_yaw),
        }

    def publish_odom_if_valid(self, data: Dict[str, float]):
        if not self.publish_odom_enabled:
            return

        if "ENC_L" not in data or "ENC_R" not in data:
            return

        current_left_encoder = int(data["ENC_L"])
        current_right_encoder = int(data["ENC_R"])
        current_time = self.get_clock().now()

        if (
            self.previous_left_encoder is None
            or self.previous_right_encoder is None
            or self.previous_odom_time is None
        ):
            self.previous_left_encoder = current_left_encoder
            self.previous_right_encoder = current_right_encoder
            self.previous_odom_time = current_time
            return

        dt = (current_time - self.previous_odom_time).nanoseconds / 1e9

        if dt <= 0:
            return

        delta_left_pulses = current_left_encoder - self.previous_left_encoder
        delta_right_pulses = current_right_encoder - self.previous_right_encoder

        left_distance_m = delta_left_pulses * self.distance_per_pulse_m
        right_distance_m = delta_right_pulses * self.distance_per_pulse_m

        center_distance_m = (left_distance_m + right_distance_m) / 2.0

        if self.wheel_track_width_m > 0:
            delta_yaw = (right_distance_m - left_distance_m) / self.wheel_track_width_m
        else:
            delta_yaw = 0.0

        self.odom_yaw += delta_yaw

        self.odom_x += center_distance_m * math.cos(self.odom_yaw)
        self.odom_y += center_distance_m * math.sin(self.odom_yaw)

        linear_velocity = center_distance_m / dt
        angular_velocity = delta_yaw / dt

        quaternion = self.yaw_to_quaternion(self.odom_yaw)

        msg = Odometry()
        msg.header.stamp = current_time.to_msg()
        msg.header.frame_id = self.odom_frame_id
        msg.child_frame_id = self.base_frame_id

        msg.pose.pose.position.x = self.odom_x
        msg.pose.pose.position.y = self.odom_y
        msg.pose.pose.position.z = 0.0

        msg.pose.pose.orientation.x = quaternion["x"]
        msg.pose.pose.orientation.y = quaternion["y"]
        msg.pose.pose.orientation.z = quaternion["z"]
        msg.pose.pose.orientation.w = quaternion["w"]

        msg.twist.twist.linear.x = linear_velocity
        msg.twist.twist.linear.y = 0.0
        msg.twist.twist.angular.z = angular_velocity

        msg.pose.covariance[0] = 0.05
        msg.pose.covariance[7] = 0.05
        msg.pose.covariance[35] = 0.10

        msg.twist.covariance[0] = 0.05
        msg.twist.covariance[35] = 0.10

        self.odom_pub.publish(msg)

        self.previous_left_encoder = current_left_encoder
        self.previous_right_encoder = current_right_encoder
        self.previous_odom_time = current_time

    def publish_sensor_data(self, data: Dict[str, float]):
        self.publish_float_if_valid_mm(data, "F_MM", self.front_pub)
        self.publish_float_if_valid_mm(data, "L_MM", self.left_pub)
        self.publish_float_if_valid_mm(data, "R_MM", self.right_pub)
        self.publish_float_if_valid_mm(data, "B_MM", self.back_pub)

        self.publish_float_if_valid(data, "TEMP_C", self.temperature_pub)
        self.publish_float_if_valid(data, "HUM_PCT", self.humidity_pub)

        self.publish_int_if_valid(data, "ENC_L", self.left_encoder_pub)
        self.publish_int_if_valid(data, "ENC_R", self.right_encoder_pub)

        self.publish_int_if_valid(data, "UPTIME_MS", self.uptime_pub)

        self.publish_imu_if_valid(data)
        self.publish_odom_if_valid(data)


def main(args=None):
    rclpy.init(args=args)

    node = SensorSerialNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node.serial_connection is not None:
            node.serial_connection.close()

        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
