# EmpwireBot Roadmap

This roadmap shows the planned development path for EmpwireBot.

---

## Current Stage

**v0.5-dev - LiDAR and Camera Upgrade**

EmpwireBot currently has motor control, sensor expansion, encoder support, ESP32 communication, and GitHub documentation started.

The current focus is preparing the robot for LiDAR, camera, mapping, and navigation.

---

## Phase 1 - Foundation

### Status

Completed

### Goals

* Build 4-wheel robot chassis
* Add motors
* Add motor drivers
* Test basic movement
* Add Raspberry Pi 5
* Add ESP32 DevKit V1
* Test serial communication
* Start ROS 2 control

---

## Phase 2 - Sensor Expansion

### Status

Completed

### Goals

* Add front distance sensor
* Add left distance sensor
* Add right distance sensor
* Add back distance sensor
* Add AHT10 temperature and humidity sensor
* Add MPU6050 IMU
* Add wheel encoders
* Create system health console
* Confirm sensor readings

---

## Phase 3 - GitHub Documentation

### Status

In Progress

### Goals

* Create GitHub repository
* Add README
* Add hardware list
* Add pin map
* Add version history
* Add development log
* Add ESP32 firmware documentation
* Add ROS 2 workspace documentation
* Add roadmap

---

## Phase 4 - LiDAR and Camera

### Status

In Progress

### Goals

* Connect LD06/LD LiDAR
* Test LiDAR data
* Connect Raspberry Pi Camera 8MP
* Test camera preview
* Add LiDAR documentation
* Add camera documentation
* Prepare ROS 2 LiDAR package
* Prepare ROS 2 camera package

---

## Phase 5 - ROS 2 Sensor Integration

### Status

Planned

### Goals

* Publish distance sensor data into ROS 2 topics
* Publish IMU data into ROS 2 topics
* Publish AHT10 data into ROS 2 topics
* Publish encoder data into ROS 2 topics
* Improve serial message format
* Improve sensor reliability

---

## Phase 6 - Odometry

### Status

Planned

### Goals

* Use wheel encoder data for odometry
* Calculate wheel speed
* Calculate robot distance travelled
* Publish odometry topic
* Improve turning accuracy
* Tune movement control

---

## Phase 7 - SLAM Mapping

### Status

Planned

### Goals

* Add LiDAR ROS 2 support
* Test LiDAR scan topic
* Start SLAM testing
* Create first map
* Save map files
* Document mapping process

---

## Phase 8 - Autonomous Navigation

### Status

Planned

### Goals

* Add ROS 2 navigation stack
* Use saved map for navigation
* Add obstacle avoidance
* Add goal-based movement
* Test autonomous driving
* Improve safety behavior

---

## Phase 9 - Vision and AI

### Status

Future

### Goals

* Use Raspberry Pi Camera for vision
* Add object detection experiments
* Add camera-based robot awareness
* Add AI-assisted behavior
* Create useful robot tasks

---

## Phase 10 - EmpwireBot v1.0

### Status

Future

### Goals

* Stable hardware
* Stable wiring
* Stable ESP32 firmware
* Stable ROS 2 packages
* Complete documentation
* GitHub release
* Demo video
* Project showcase

