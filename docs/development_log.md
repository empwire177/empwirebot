# EmpwireBot Development Log

This file records important development progress, tests, fixes, and hardware changes for EmpwireBot.

---

## 2026-07-06 - GitHub Repository Setup

### Completed

* Created EmpwireBot GitHub repository
* Connected local Mac folder to GitHub
* Added project folder structure
* Added `.gitignore`
* Added main `README.md`
* Added current hardware list
* Added pin map
* Added version history

### Notes

This is the official start of the EmpwireBot GitHub documentation system.

---

## Current Development Stage

**EmpwireBot v0.5-dev - LiDAR and Camera Upgrade**

### Current Focus

* Organising GitHub repository
* Documenting hardware
* Preparing for LiDAR testing
* Preparing for Raspberry Pi Camera testing
* Preparing future ROS 2 sensor integration

---

## Recent Hardware Progress

### Added / Confirmed Hardware

* Raspberry Pi 5
* ESP32 DevKit V1
* 4-wheel robot chassis
* 2 x L298N motor drivers
* 4 x TT DC gear motors
* 4 x VL53 distance sensors
* MPU6050 IMU
* AHT10 temperature and humidity sensor
* Wheel encoders
* LD06/LD LiDAR
* Raspberry Pi Camera 8MP

---

## Recent Software Progress

### GitHub

* Repository created
* Project folder structure added
* Documentation started

### ROS 2

* ROS 2 Jazzy used on Raspberry Pi 5
* Motor control system already tested
* Sensor serial system already tested

### ESP32

* ESP32 used for motor and sensor side
* USB serial communication used between ESP32 and Raspberry Pi 5

---

## Next Planned Work

### Short-Term Goals

* Add ESP32 firmware files to GitHub
* Add ROS 2 package files to GitHub
* Test LD06/LD LiDAR wiring
* Test Raspberry Pi Camera 8MP
* Update documentation after each successful test

### Future Goals

* Add LiDAR data to ROS 2
* Add camera testing documentation
* Improve encoder-based odometry
* Start SLAM testing
* Prepare autonomous navigation

