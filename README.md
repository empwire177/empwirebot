# EmpwireBot

![Project Status](https://img.shields.io/badge/status-v0.5--dev-orange)
![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi%205%20%2B%20ESP32-blue)
![ROS 2](https://img.shields.io/badge/ROS%202-Jazzy-purple)
![License](https://img.shields.io/badge/license-MIT-green)

## Project Status Summary

**Current Version:** v0.5-dev - LiDAR and Camera Upgrade
**Main Controller:** Raspberry Pi 5
**Low-Level Controller:** ESP32 DevKit V1
**ROS 2 Version:** ROS 2 Jazzy
**Current Focus:** LiDAR, camera, ROS 2 sensor integration, odometry, and future SLAM preparation

### Current Status

| Area                     | Status                           |
| ------------------------ | -------------------------------- |
| GitHub repository        | Working                          |
| Documentation            | In progress                      |
| ESP32 firmware           | Working / improving              |
| ROS 2 sensor package     | Starter package added            |
| Motor control            | Working                          |
| Distance sensors         | Working                          |
| MPU6050 IMU              | Working                          |
| AHT10 sensor             | Working                          |
| Wheel encoders           | Working                          |
| Basic `/odom` publishing | Added                            |
| LD06/LD LiDAR            | Hardware added / testing pending |
| Raspberry Pi Camera 8MP  | Hardware added / testing pending |
| SLAM and navigation      | Planned                          |



EmpwireBot is my personal robotics project using Raspberry Pi 5, ESP32, ROS 2, sensors, motor control, LiDAR, camera, and autonomous navigation.

## Current Version

**EmpwireBot v0.5-dev - LiDAR and Camera Upgrade**

EmpwireBot is currently moving from sensor expansion into LiDAR, camera, mapping, and future navigation development.

---

## Current Hardware

The full current hardware list is here:

[Current Hardware List](hardware/current_hardware.md)

Main hardware includes:

* Raspberry Pi 5
* ESP32 DevKit V1
* 4-wheel robot chassis
* 4 x TT DC gear motors
* 2 x L298N motor drivers
* 4 x distance sensors
* MPU6050 IMU
* AHT10 temperature and humidity sensor
* Wheel encoders
* LD06/LD LiDAR
* Raspberry Pi Camera 8MP

---
## Documentation

- [Current Hardware List](hardware/current_hardware.md)
- [Pin Map](hardware/pin_map.md)
- [System Architecture](docs/system_architecture.md)
- [Version History](docs/version_history.md)
- [Development Log](docs/development_log.md)
- [Roadmap](docs/roadmap.md)
- [LiDAR Setup Notes](docs/lidar_setup.md)
- [Camera Setup Notes](docs/camera_setup.md)
- [ESP32 Firmware Notes](firmware/esp32/README.md)
- [ROS 2 Workspace Notes](ros2_ws/src/README.md)
- [Software Status](docs/software_status.md)
- [Testing Checklist](docs/testing_checklist.md)
- [Changelog](CHANGELOG.md)
- [Changelog](CHANGELOG.md)
- [Contributing Guide](CONTRIBUTING.md)
- [License](LICENSE)
- [Serial Protocol](docs/serial_protocol.md)
- [ROS 2 Sensor Parser Plan](docs/ros2_sensor_parser_plan.md)
- [Encoder Odometry Plan](docs/encoder_odometry_plan.md)
- [ROS 2 Sensor Package Test Guide](docs/ros2_sensor_package_test_guide.md)
- [Current Tasks](docs/current_tasks.md)



---

## Project Goals

* Manual control
* ROS 2 motor control
* ESP32 sensor and motor communication
* System health monitoring
* Obstacle avoidance
* Encoder-based odometry
* LiDAR mapping
* Camera vision
* Autonomous navigation
* Future AI features

---

## Current Development Stage

EmpwireBot is currently in the **v0.5-dev LiDAR and Camera Upgrade** stage.

The next development goals are:

1. Test LD06/LD LiDAR connection
2. Test Raspberry Pi Camera 8MP
3. Add LiDAR data into ROS 2
4. Add camera testing documentation
5. Prepare for SLAM and mapping

---

## Repository Structure

```text
empwirebot/

 docs/

   
 camera_setup.md

   
 development_log.md

   
 lidar_setup.md

   
 roadmap.md

   
 version_history.md

 firmware/

   
 esp32/

 hardware/

   
 current_hardware.md

   
 pin_map.md

 images/

 ros2_ws/

   
 src/

 .gitignore

 README.md
```

---

## Notes

This repository is the official development home for EmpwireBot.

