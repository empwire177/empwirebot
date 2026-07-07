# EmpwireBot Current Tasks

This file tracks the current active tasks for EmpwireBot.

---

## Current Version

**EmpwireBot v0.5-dev - LiDAR and Camera Upgrade**

---

## High Priority Tasks

### 1. Test ESP32 Sensor Serial Firmware

Status: **Pending Raspberry Pi test**

Tasks:

* [ ] Upload `sensor_serial_v2_1.ino` to ESP32
* [ ] Open Arduino Serial Monitor
* [ ] Confirm `SENSOR,` lines are printing
* [ ] Confirm front distance value
* [ ] Confirm left distance value
* [ ] Confirm right distance value
* [ ] Confirm back distance value
* [ ] Confirm AHT10 temperature and humidity
* [ ] Confirm MPU6050 values
* [ ] Confirm encoder counts

---

### 2. Test ROS 2 Sensor Package

Status: **Pending Raspberry Pi test**

Tasks:

* [ ] Clone/pull latest GitHub repo on Raspberry Pi 5
* [ ] Build `empwirebot_sensors`
* [ ] Source ROS 2 workspace
* [ ] Run `sensor_serial_node`
* [ ] Check `/distance/front`
* [ ] Check `/distance/left`
* [ ] Check `/distance/right`
* [ ] Check `/distance/back`
* [ ] Check `/aht10/temperature`
* [ ] Check `/aht10/humidity`
* [ ] Check `/encoder/left`
* [ ] Check `/encoder/right`
* [ ] Check `/imu/data`
* [ ] Check `/odom`

---

### 3. Test LD06/LD LiDAR

Status: **Hardware added / wiring pending**

Tasks:

* [ ] Confirm LiDAR wire colours
* [ ] Confirm LiDAR voltage
* [ ] Confirm GND
* [ ] Confirm TX
* [ ] Confirm RX
* [ ] Choose connection method
* [ ] Test raw serial data
* [ ] Find ROS 2 driver
* [ ] Publish `/scan`
* [ ] View LiDAR in RViz

---

### 4. Test Raspberry Pi Camera 8MP

Status: **Hardware added / testing pending**

Tasks:

* [ ] Connect camera ribbon cable
* [ ] Check camera detection
* [ ] Test preview
* [ ] Capture test image
* [ ] Capture test video
* [ ] Add camera notes to documentation
* [ ] Prepare ROS 2 camera support

---

## Medium Priority Tasks

### 5. Improve Encoder Odometry

Status: **Basic `/odom` added**

Tasks:

* [ ] Test `/odom` topic
* [ ] Measure wheel track width
* [ ] Add `wheel_track_width_m`
* [ ] Improve turning calculation
* [ ] Add wheel direction support
* [ ] Add TF support
* [ ] Test odometry while driving

---

### 6. Improve ROS 2 Sensor Node

Status: **Starter package added**

Tasks:

* [ ] Add better serial reconnect handling
* [ ] Add launch parameter documentation
* [ ] Add IMU calibration notes
* [ ] Add odometry tuning notes
* [ ] Add test launch file
* [ ] Add sample serial data file

---

### 7. Add Images and Diagrams

Status: **Planned**

Tasks:

* [ ] Add robot photo
* [ ] Add wiring diagram
* [ ] Add system architecture image
* [ ] Add sensor layout image
* [ ] Add GitHub README project image

---

## Future Tasks

### 8. SLAM Preparation

Status: **Future**

Tasks:

* [ ] Get LiDAR `/scan` working
* [ ] Get `/odom` working better
* [ ] Check TF tree
* [ ] Install SLAM package
* [ ] Create first map
* [ ] Save map

---

### 9. Navigation Preparation

Status: **Future**

Tasks:

* [ ] Add Nav2
* [ ] Load saved map
* [ ] Test robot localisation
* [ ] Send navigation goal
* [ ] Improve obstacle avoidance
* [ ] Test autonomous movement

---

## Current Main Focus

The current main focus is:

1. Test ESP32 sensor firmware on real hardware
2. Test ROS 2 sensor package on Raspberry Pi 5
3. Start LiDAR wiring/testing
4. Start Raspberry Pi Camera testing

