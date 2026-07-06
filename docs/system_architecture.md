# EmpwireBot System Architecture

This document explains the main system architecture of EmpwireBot.

---

## Overview

EmpwireBot uses a two-controller architecture:

* Raspberry Pi 5 for high-level control
* ESP32 DevKit V1 for low-level motor and sensor control

The Raspberry Pi 5 runs ROS 2 and handles the main robot intelligence.

The ESP32 handles motor control, sensor readings, encoder counting, and serial communication.

---

## Main Architecture Diagram

```text
                    Raspberry Pi 5
              Ubuntu 24.04 + ROS 2 Jazzy
                           |
                           | USB Serial
                           |
                    ESP32 DevKit V1
                           |
        ------------------------------------------------
        |              |              |                |
   Motor Drivers   Distance Sensors   IMU/AHT10     Encoders
        |              |              |                |
   4 DC Motors     Front/Left/Right/Back Sensors    Wheels
```

---

## Raspberry Pi 5 Responsibilities

The Raspberry Pi 5 is the main computer of EmpwireBot.

It is responsible for:

* Running Ubuntu 24.04
* Running ROS 2 Jazzy
* Receiving joystick/keyboard/GUI commands
* Sending movement commands to the ESP32
* Receiving sensor data from the ESP32
* Processing LiDAR data
* Processing camera data
* Future SLAM mapping
* Future autonomous navigation
* Future AI features

---

## ESP32 DevKit V1 Responsibilities

The ESP32 is the low-level controller.

It is responsible for:

* Controlling the L298N motor drivers
* Driving the 4 DC motors
* Reading distance sensors
* Reading MPU6050 IMU data
* Reading AHT10 temperature and humidity data
* Counting wheel encoder pulses
* Sending system health data to the Raspberry Pi
* Receiving motor commands from the Raspberry Pi

---

## Communication Flow

### Motor Command Flow

```text
ROS 2 /cmd_vel
      |
      v
Raspberry Pi 5 ROS 2 motor serial node
      |
      v
USB Serial
      |
      v
ESP32
      |
      v
L298N Motor Drivers
      |
      v
4 DC Motors
```

### Sensor Data Flow

```text
Distance Sensors / IMU / AHT10 / Encoders
      |
      v
ESP32
      |
      v
USB Serial
      |
      v
Raspberry Pi 5
      |
      v
ROS 2 sensor nodes
      |
      v
ROS 2 topics
```

---

## Sensor System

Current sensor system includes:

* Front distance sensor
* Left distance sensor
* Right distance sensor
* Back distance sensor
* MPU6050 IMU
* AHT10 temperature and humidity sensor
* Left wheel encoder
* Right wheel encoder
* LD06/LD LiDAR
* Raspberry Pi Camera 8MP

---

## ROS 2 System

EmpwireBot uses ROS 2 Jazzy.

Current or planned ROS 2 nodes/packages include:

* Motor control node
* Motor serial node
* Sensor serial node
* Robot serial node
* GUI control panel
* LiDAR node
* Camera node
* Odometry node
* SLAM node
* Navigation node

---

## Current Development Stage

EmpwireBot is currently in:

**v0.5-dev - LiDAR and Camera Upgrade**

The current architecture is already suitable for:

* Manual robot control
* ESP32 serial communication
* Sensor monitoring
* System health checking
* Future ROS 2 sensor publishing
* Future SLAM and navigation

---

## Future Architecture Goals

Future improvements may include:

* Cleaner serial message protocol
* Dedicated ROS 2 topics for each sensor
* Encoder-based odometry
* LiDAR `/scan` topic
* Camera `/image_raw` topic
* SLAM mapping
* Autonomous navigation
* Object detection
* AI-assisted robot behavior

