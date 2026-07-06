# EmpwireBot Testing Checklist

This checklist is used to test EmpwireBot hardware, firmware, ROS 2 nodes, sensors, LiDAR, camera, and navigation features.

---

## Current Version

**EmpwireBot v0.5-dev - LiDAR and Camera Upgrade**

---

## 1. Power Safety Check

### Checklist

* [ ] Battery voltage checked
* [ ] Raspberry Pi 5 power supply checked
* [ ] ESP32 power checked
* [ ] Motor driver power checked
* [ ] Common GND checked
* [ ] No loose wires
* [ ] No overheating parts
* [ ] Robot lifted from ground before motor test

---

## 2. Motor Test

### Checklist

* [ ] Front left motor moves forward
* [ ] Front right motor moves forward
* [ ] Rear left motor moves forward
* [ ] Rear right motor moves forward
* [ ] All motors move forward together
* [ ] All motors move backward together
* [ ] Robot turns left
* [ ] Robot turns right
* [ ] Robot stops correctly

### Status

Current status: **Working**

---

## 3. ESP32 Serial Test

### Checklist

* [ ] ESP32 detected by Raspberry Pi
* [ ] Correct serial port found
* [ ] Serial data readable
* [ ] Raspberry Pi can send command to ESP32
* [ ] ESP32 can send sensor data to Raspberry Pi

### Status

Current status: **Working**

---

## 4. Distance Sensor Test

### Checklist

* [ ] Front distance sensor working
* [ ] Left distance sensor working
* [ ] Right distance sensor working
* [ ] Back distance sensor working
* [ ] Sensor values change when hand/object is moved
* [ ] Out-of-range values handled correctly

### Status

Current status: **Working**

---

## 5. MPU6050 IMU Test

### Checklist

* [ ] Accelerometer readings working
* [ ] Gyroscope readings working
* [ ] Angle output working
* [ ] Values change when robot is tilted
* [ ] Robot flat position readings checked

### Status

Current status: **Working**

---

## 6. AHT10 Sensor Test

### Checklist

* [ ] Temperature reading working
* [ ] Humidity reading working
* [ ] Values are reasonable
* [ ] Sensor appears in system health output

### Status

Current status: **Working**

---

## 7. Wheel Encoder Test

### Checklist

* [ ] Left encoder pulse reading working
* [ ] Right encoder pulse reading working
* [ ] Pulse count increases when wheels move
* [ ] 20 pulses per wheel rotation confirmed
* [ ] Wheel diameter recorded as 67.6 mm
* [ ] Speed calculation tested
* [ ] Odometry calculation tested

### Status

Current status: **Working / Odometry planned**

---

## 8. ROS 2 Motor Control Test

### Checklist

* [ ] ROS 2 environment sourced
* [ ] Motor node starts
* [ ] Teleop keyboard sends `/cmd_vel`
* [ ] Robot responds to forward command
* [ ] Robot responds to turn command
* [ ] Robot stops when command stops
* [ ] GUI control panel works

### Status

Current status: **Working**

---

## 9. ROS 2 Sensor Test

### Checklist

* [ ] Sensor serial node starts
* [ ] ESP32 sensor data received
* [ ] Distance sensor data parsed correctly
* [ ] IMU data parsed correctly
* [ ] AHT10 data parsed correctly
* [ ] Encoder data parsed correctly
* [ ] Sensor data published to ROS 2 topics

### Status

Current status: **Partly working / ROS 2 topic publishing planned**

---

## 10. LiDAR Test

### Checklist

* [ ] LiDAR wire colours/signals confirmed
* [ ] LiDAR voltage confirmed
* [ ] LiDAR GND connected correctly
* [ ] LiDAR serial data received
* [ ] LiDAR baud rate confirmed
* [ ] ROS 2 LiDAR driver tested
* [ ] `/scan` topic published
* [ ] LiDAR data visible in RViz

### Status

Current status: **Hardware added / testing pending**

---

## 11. Camera Test

### Checklist

* [ ] Camera connected to Raspberry Pi 5
* [ ] Camera detected
* [ ] Preview working
* [ ] Test image captured
* [ ] Test video captured
* [ ] ROS 2 camera topic tested
* [ ] Camera feed visible

### Status

Current status: **Hardware added / testing pending**

---

## 12. SLAM and Navigation Test

### Checklist

* [ ] LiDAR `/scan` topic working
* [ ] Odometry topic working
* [ ] TF tree working
* [ ] SLAM package installed
* [ ] First map created
* [ ] Map saved
* [ ] Navigation stack tested
* [ ] Robot moves to goal

### Status

Current status: **Future planned**

---

## Test Log Notes

Use this section to record test results.

### Latest Test

Date:

Result:

Notes:

