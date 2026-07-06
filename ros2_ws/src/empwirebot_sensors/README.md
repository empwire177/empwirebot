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



Run Command:
ros2 run empwirebot_sensors sensor_serial_node

With custom serial port:
ros2 run empwirebot_sensors sensor_serial_node --ros-args -p port:=/dev/ttyUSB0


Build Command
From the ROS 2 workspace root: 

colcon build --packages-select empwirebot_sensors
source install/setup.bash

Notes
This is the starter ROS 2 sensor parser package for EmpwireBot v0.5-dev.


