# EmpwireBot ROS 2 Sensor Parser Plan

This document explains the plan for parsing ESP32 sensor serial data into ROS 2 topics.

---

## Purpose

EmpwireBot uses the ESP32 DevKit V1 to read low-level sensors.

The ESP32 sends sensor data to the Raspberry Pi 5 over USB serial.

The Raspberry Pi 5 will run a ROS 2 Python node that reads this serial data, parses it, and publishes sensor values into ROS 2 topics.

---

## Current ESP32 Serial Format

The ESP32 outputs one line starting with:

```text
SENSOR,
```

Example:

```text
SENSOR,F_MM=320,L_MM=450,R_MM=390,B_MM=600,TEMP_C=25.40,HUM_PCT=48.20,MPU_OK=1,AX_G=0.010,AY_G=0.020,AZ_G=1.000,GX_DPS=0.100,GY_DPS=-0.050,GZ_DPS=0.020,MPU_TEMP_C=31.25,ENC_L=120,ENC_R=118,UPTIME_MS=5000
```

---

## Parser Responsibilities

The ROS 2 sensor parser node should:

1. Open the ESP32 serial port.
2. Read one full line at a time.
3. Ignore lines that do not start with `SENSOR,`.
4. Split the line by commas.
5. Split each field by `=`.
6. Convert values into numbers.
7. Handle missing fields safely.
8. Handle invalid values safely.
9. Publish valid data into ROS 2 topics.
10. Keep running even if one serial line has an error.

---

## Planned Node Name

Possible ROS 2 node name:

```text
sensor_serial_node
```

Possible package name:

```text
empwirebot_sensors
```

---

## Planned ROS 2 Topics

### Distance Topics

| Sensor         | Serial Field | ROS 2 Topic       | Message Type           |
| -------------- | ------------ | ----------------- | ---------------------- |
| Front distance | `F_MM`       | `/distance/front` | `std_msgs/msg/Float32` |
| Left distance  | `L_MM`       | `/distance/left`  | `std_msgs/msg/Float32` |
| Right distance | `R_MM`       | `/distance/right` | `std_msgs/msg/Float32` |
| Back distance  | `B_MM`       | `/distance/back`  | `std_msgs/msg/Float32` |

Distance values should be published in metres.

Example conversion:

```text
320 mm = 0.320 m
```

If the ESP32 sends `-1`, the value should be treated as invalid or out of range.

---

## AHT10 Topics

| Sensor Value | Serial Field | ROS 2 Topic          | Message Type           |
| ------------ | ------------ | -------------------- | ---------------------- |
| Temperature  | `TEMP_C`     | `/aht10/temperature` | `std_msgs/msg/Float32` |
| Humidity     | `HUM_PCT`    | `/aht10/humidity`    | `std_msgs/msg/Float32` |

If the ESP32 sends `-999.00`, the value should be treated as invalid.

---

## IMU Topic

Serial fields:

```text
AX_G
AY_G
AZ_G
GX_DPS
GY_DPS
GZ_DPS
MPU_OK
```

Planned topic:

```text
/imu/data
```

Planned message type:

```text
sensor_msgs/msg/Imu
```

Important notes:

* Only publish IMU data when `MPU_OK=1`.
* Accelerometer data is currently in g.
* Gyroscope data is currently in degrees per second.
* ROS 2 IMU messages normally use:


  * angular velocity in rad/s

Planned conversions:

```text
acceleration_mps2 = acceleration_g * 9.80665
angular_velocity_radps = gyro_dps * 0.0174533
```

Orientation data is not confirmed yet, so orientation covariance should show that orientation is unknown.

---

## Encoder Topics

Serial fields:

```text
ENC_L
ENC_R
```

Planned simple topics:

| Encoder       | ROS 2 Topic      | Message Type         |
| ------------- | ---------------- | -------------------- |
| Left encoder  | `/encoder/left`  | `std_msgs/msg/Int64` |
| Right encoder | `/encoder/right` | `std_msgs/msg/Int64` |

Future odometry topic:

```text
/odom
```

Planned message type:

```text
nav_msgs/msg/Odometry
```

Known encoder details:

* 20 pulses per wheel rotation
* Wheel diameter: 67.6 mm

Wheel circumference calculation:

```text
circumference = pi * diameter
circumference = pi * 0.0676 m
circumference   * acceleration in m/s
 0.2124 m
```

Distance per pulse:

```text
distance_per_pulse = 0.2124 / 20
distance_per_pulse 
 0.01062 m
```

---

## Uptime Topic

Serial field:

```text
UPTIME_MS
```

Possible topic:

```text
/esp32/uptime_ms
```

Message type:

```text
std_msgs/msg/Int64
```

---

## Error Handling Rules

The parser should:

* Ignore empty lines.
* Ignore non-`SENSOR` lines.
* Catch parse errors.
* Keep the node running after bad data.
* Log warnings for bad lines.
* Not crash if one field is missing.
* Not crash if a value is not numeric.
* Treat distance `-1` as invalid.
* Treat AHT10 `-999.00` as invalid.
* Publish IMU only when `MPU_OK=1`.

---

## First Implementation Goal

The first version of the ROS 2 parser should publish:

* `/distance/front`
* `/distance/left`
* `/distance/right`
* `/distance/back`
* `/aht10/temperature`
* `/aht10/humidity`
* `/encoder/left`
* `/encoder/right`

After that, add:

* `/imu/data`
* `/odom`

---

## Test Commands

Possible future test commands:

```bash
ros2 run empwirebot_sensors sensor_serial_node
```

Check topics:

```bash
ros2 topic list
```

Check front distance:

```bash
ros2 topic echo /distance/front
```

Check temperature:

```bash
ros2 topic echo /aht10/temperature
```

Check encoder:

```bash
ros2 topic echo /encoder/left
```

---

## Current Status

Status: **Planned**

This document is the design plan before adding the real ROS 2 Python parser node.

---

## Related Files

Serial protocol:

```text
docs/serial_protocol.md
```

Current ESP32 firmware:

```text
firmware/esp32/sensor_serial_v2_1/sensor_serial_v2_1.ino
```

ROS 2 package index:

```text
ros2_ws/src/ROS2_PACKAGE_INDEX.md
```

