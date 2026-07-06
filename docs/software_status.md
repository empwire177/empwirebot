# EmpwireBot Software Status

This document tracks the current software status of EmpwireBot.

---

## Current Development Version

**EmpwireBot v0.5-dev - LiDAR and Camera Upgrade**

---

## Working Software

### GitHub Repository

Status: **Working**

Completed:

* Repository created
* Local Mac folder connected to GitHub
* Project folder structure created
* `.gitignore` added
* README added
* Hardware list added
* Pin map added
* Version history added
* Development log added
* Roadmap added
* System architecture added

---

### ESP32 Firmware

Status: **Working / In Progress**

Working:

* ESP32 DevKit V1 connected
* Motor control tested
* Sensor reading tested
* System health console tested
* Wheel encoder reading tested
* USB serial communication with Raspberry Pi tested

In progress:

* Organising firmware files
* Preparing cleaner firmware structure for GitHub
* Preparing ROS 2 sensor integration

---

### ROS 2 System

Status: **Working / In Progress**

Working:

* ROS 2 Jazzy installed on Raspberry Pi 5
* `/cmd_vel` control tested
* Teleop keyboard control tested
* Motor node tested
* Motor serial node tested
* Sensor serial node tested
* Robot serial node tested
* GUI control panel tested

In progress:

* Adding ROS 2 package files to GitHub
* Improving sensor serial node
* Preparing LiDAR ROS 2 support
* Preparing camera ROS 2 support

---

## Hardware-Related Software

### Motor Control

Status: **Working**

Working:

* 4-wheel movement
* Forward movement
* Manual control
* ROS 2 command control
* ESP32 motor control

---

### Distance Sensors

Status: **Working**

Working:

* Front distance sensor
* Left distance sensor
* Right distance sensor
* Back distance sensor
* System health output

---

### MPU6050 IMU

Status: **Working**

Working:

* Accelerometer readings
* Gyroscope readings
* Angle output testing

---

### AHT10 Sensor

Status: **Working**

Working:

* Temperature reading
* Humidity reading

---

### Wheel Encoders

Status: **Working**

Working:

* Left encoder pulse reading
* Right encoder pulse reading
* 20 pulses per wheel rotation confirmed
* Wheel diameter documented as 67.6 mm

Planned:

* Encoder speed calculation
* Encoder odometry
* ROS 2 odometry publishing

---

### LD06/LD LiDAR

Status: **Hardware Added / Testing Pending**

Planned:

* Confirm wiring
* Confirm voltage
* Test serial data
* Add ROS 2 LiDAR support
* Publish `/scan`
* Use for SLAM

---

### Raspberry Pi Camera 8MP

Status: **Hardware Added / Testing Pending**

Planned:

* Test camera detection
* Test image capture
* Test video capture
* Add ROS 2 camera support
* Prepare future vision experiments

---

## Planned Software Work

Short-term:

* Add ESP32 firmware files
* Add ROS 2 package files
* Add LiDAR test notes
* Add camera test notes
* Improve documentation

Medium-term:

* Publish sensor data to ROS 2 topics
* Improve encoder odometry
* Add LiDAR scan topic
* Add camera image topic
* Start SLAM testing

Long-term:

* Autonomous navigation
* Vision features
* AI-assisted behavior
* EmpwireBot v1.0 stable release

