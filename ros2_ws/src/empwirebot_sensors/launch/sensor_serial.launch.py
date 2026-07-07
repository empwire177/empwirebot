from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    port_arg = DeclareLaunchArgument(
        "port",
        default_value="/dev/ttyUSB0",
        description="Serial port connected to ESP32",
    )

    baudrate_arg = DeclareLaunchArgument(
        "baudrate",
        default_value="115200",
        description="ESP32 serial baud rate",
    )

    sensor_node = Node(
        package="empwirebot_sensors",
        executable="sensor_serial_node",
        name="sensor_serial_node",
        output="screen",
        parameters=[
            {
                "port": LaunchConfiguration("port"),
                "baudrate": LaunchConfiguration("baudrate"),
            }
        ],
    )

    return LaunchDescription([
        port_arg,
        baudrate_arg,
        sensor_node,
    ])
