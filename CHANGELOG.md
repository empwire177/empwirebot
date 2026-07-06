# EmpwireBot Changelog

All important changes to EmpwireBot will be documented in this file.

---

## v0.5-dev - LiDAR and Camera Upgrade

### Status

In Progress

### Added

* Added LD06/LD LiDAR to hardware list
* Added Raspberry Pi Camera 8MP to hardware list
* Added LiDAR setup notes
* Added camera setup notes
* Added system architecture documentation
* Added software status documentation
* Added testing checklist
* Added ESP32 sensor serial firmware v2.1
* Confirmed back distance sensor XSHUT pin as GPIO15

### Changed

* Updated main README with documentation links
* Updated ESP32 firmware documentation
* Updated hardware pin map

### Planned

* Test LD06/LD LiDAR wiring
* Test LiDAR serial data
* Test Raspberry Pi Camera detection
* Add LiDAR ROS 2 support
* Add camera ROS 2 support
* Prepare for SLAM and mapping

---

## v0.4 - Sensor Expansion Stage

### Status

Completed

### Added

* Added four-side distance sensor system
* Added front distance sensor
* Added left distance sensor
* Added right distance sensor
* Added back distance sensor
* Added AHT10 temperature and humidity sensor
* Added MPU6050 IMU
* Added left and right wheel encoders
* Added system health console testing

### Confirmed

* Distance sensors working
* AHT10 working
* MPU6050 readings working
* Wheel encoder pulses working
* 20 pulses per wheel rotation confirmed
* Wheel diameter documented as 67.6 mm

---

## v0.3 - ESP32 Serial Control

### Status

Completed

### Added

* Added ESP32 DevKit V1 as low-level controller
* Added USB serial communication between Raspberry Pi 5 and ESP32
* Added ESP32 motor/sensor role
* Added serial communication testing

### Confirmed

* Raspberry Pi 5 can communicate with ESP32
* ESP32 can handle motor and sensor-side tasks

---

## v0.2 - Raspberry Pi and ROS 2 Control

### Status

Completed

### Added

* Added Raspberry Pi 5 as main robot computer
* Installed Ubuntu 24.04
* Installed ROS 2 Jazzy
* Added ROS 2 motor control
* Added teleop keyboard control
* Added GUI control panel testing

### Confirmed

* `/cmd_vel` control working
* Motor node working
* Teleop control working
* GUI control working

---

## v0.1 - Basic Motor Control

### Status

Completed

### Added

* Built 4-wheel robot chassis
* Added 4 x TT DC gear motors
* Added 2 x L298N motor drivers
* Tested basic motor movement

### Confirmed

* Motors can move
* Basic robot drive system works

