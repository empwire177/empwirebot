# empwirebot_sensors

ROS 2 sensor package for EmpwireBot.

This package reads ESP32 serial sensor data and publishes it into ROS 2 topics.

## Current Node

### sensor_serial_node

Reads serial data from the ESP32.

Default serial port:

```text
/dev/ttyUSB0

Default baud rate:115200

Published Topics:

/distance/front
/distance/left
/distance/right
/distance/back
/aht10/temperature
/aht10/humidity
/encoder/left
/encoder/right
/esp32/uptime_ms
/imu/data
/odom

## Odometry

The node publishes basic encoder odometry to:

```text
/odom

Current encoder settings:  
pulses_per_revolution = 20
wheel_diameter_m = 0.0676


The calculated distance per encoder pulse is about:
0.01062 m

Important current limitation:
The encoder system currently counts pulses only. It does not yet know wheel direction, so /odom is basic and should be improved later using motor direction or better encoder direction sensing.

Wheel track width is not confirmed yet, so turning odometry is disabled by default.

Later, set: 
wheel_track_width_m

to enable better turning calculation.


## IMU Data

The node publishes MPU6050 data to:

```text
/imu/data

The ESP32 sends acceleration in g and gyro values in degrees per second.
The ROS 2 node converts:

acceleration g -> m/s²
gyro deg/s -> rad/s

Run Command:
## Launch Command

```bash
ros2 launch empwirebot_sensors sensor_serial.launch.py

ros2 run empwirebot_sensors sensor_serial_node

With custom serial port:
ros2 launch empwirebot_sensors sensor_serial.launch.py port:=/dev/ttyUSB0
ros2 run empwirebot_sensors sensor_serial_node --ros-args -p port:=/dev/ttyUSB0


Build Command
From the ROS 2 workspace root: 

colcon build --packages-select empwirebot_sensors
source install/setup.bash

Notes
This is the starter ROS 2 sensor parser package for EmpwireBot v0.5-dev.


