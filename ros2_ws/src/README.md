# EmpwireBot ROS 2 Workspace

This folder is for EmpwireBot ROS 2 packages.

EmpwireBot uses ROS 2 on Raspberry Pi 5 for high-level robot control, sensor communication, odometry, LiDAR, camera, mapping, and future autonomous navigation.

## ROS 2 Version

EmpwireBot currently uses:

* Ubuntu 24.04
* ROS 2 Jazzy

## Raspberry Pi 5 Role

The Raspberry Pi 5 is used as the main robot computer.

It handles:

* ROS 2 nodes
* Motor command publishing
* Sensor data processing
* LiDAR processing
* Camera processing
* Odometry
* Mapping
* Future autonomous navigation
* Future AI features

## ESP32 Communication

The Raspberry Pi 5 communicates with the ESP32 DevKit V1 using USB serial.

The ESP32 handles:

* Motor control
* Distance sensors
* MPU6050 IMU
* AHT10 sensor
* Wheel encoders

The Raspberry Pi receives ESP32 data and can publish it into ROS 2 topics.

## Current / Planned ROS 2 Packages

Future ROS 2 packages may include:

* `empwirebot_bringup`
* `empwirebot_description`
* `empwirebot_control`
* `empwirebot_sensors`
* `empwirebot_navigation`
* `empwirebot_camera`
* `empwirebot_lidar`

## Current Working Nodes

EmpwireBot has already tested:

* Motor control node
* Motor serial node
* Sensor serial node
* Robot serial node
* GUI control panel
* Teleop keyboard control using `/cmd_vel`

## Planned ROS 2 Work

Short-term goals:

* Add existing ROS 2 package files to GitHub
* Improve `empwirebot_sensors`
* Publish ESP32 sensor data into ROS 2 topics
* Add encoder odometry improvements
* Add LiDAR ROS 2 support
* Add camera testing support

Long-term goals:

* SLAM mapping
* Navigation stack
* Autonomous driving
* Vision-based features
* AI-assisted robot behavior

## Notes

ROS 2 build folders should not be committed to GitHub.

These folders are ignored by `.gitignore`:

* `build/`
* `install/`
* `log/`

