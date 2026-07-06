# EmpwireBot Version History

This file tracks the development progress of EmpwireBot.

## Version System

EmpwireBot uses versions like:

v0.1, v0.2, v0.3, v0.4

During early development, EmpwireBot will use v0.x versions.

---

## v0.1 - Basic Motor Control

### Status

Completed

### Main Features

* 4-wheel chassis assembled
* TT DC motors connected
* L298N motor drivers tested
* Basic motor movement confirmed

---

## v0.2 - Raspberry Pi and ROS 2 Control

### Status

Completed

### Main Features

* Raspberry Pi 5 added as main controller
* ROS 2 Jazzy installed
* /cmd_vel control tested
* Teleop keyboard control working
* Motor node working

---

## v0.3 - ESP32 Serial Control

### Status

Completed

### Main Features

* ESP32 DevKit V1 added
* ESP32 connected to Raspberry Pi using USB serial
* Motor serial control tested
* ROS 2 to ESP32 communication working

---

## v0.4 - Sensor Expansion Stage

### Status

Completed

### Main Features

* Four-side distance sensor system added
* Front, left, right, and back distance sensors added
* AHT10 temperature and humidity sensor added
* MPU6050 IMU added
* Wheel encoders added
* System health console tested

---

## v0.5-dev - LiDAR and Camera Upgrade

### Status

In Progress

### Planned / Current Features

* LD06/LD LiDAR added to hardware list
* Raspberry Pi Camera 8MP added
* LiDAR connection and testing
* Camera testing
* Future SLAM preparation
* Future navigation stack preparation

---

## Future Versions

### v0.6 - ROS 2 Sensor Integration

* Publish sensor data into ROS 2 topics
* Improve sensor serial node
* Add encoder-based odometry improvements

### v0.7 - LiDAR Mapping

* Add LiDAR ROS 2 node
* Start SLAM testing
* Create first map

### v0.8 - Autonomous Navigation

* Add navigation stack
* Obstacle avoidance with LiDAR
* Basic autonomous driving

### v1.0 - First Stable EmpwireBot

* Stable hardware
* Stable ROS 2 software
* Proper documentation
* GitHub release

