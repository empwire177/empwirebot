# EmpwireBot ROS 2 Package Index

This file lists the current and planned ROS 2 packages for EmpwireBot.

---

## ROS 2 Environment

EmpwireBot currently uses:

* Ubuntu 24.04
* ROS 2 Jazzy
* Raspberry Pi 5 as the main robot computer
* ESP32 DevKit V1 as the low-level controller

---

## Current ROS 2 Workspace

Workspace location:

```text
ros2_ws/
```

Source folder:

```text
ros2_ws/src/
```

---

## Current / Tested ROS 2 Nodes

EmpwireBot has already tested these ROS 2 parts:

### motor_node

Status: **Working**

Purpose:

* Receives `/cmd_vel`
* Controls motor movement
* Supports manual robot movement
* Works with teleop keyboard and GUI control

---

### motor_serial_node

Status: **Working**

Purpose:

* Receives ROS 2 movement commands
* Sends motor commands to ESP32 over USB serial
* Allows Raspberry Pi 5 to control ESP32 motor side

---

### sensor_serial_node

Status: **Working / Improving**

Purpose:

* Reads ESP32 sensor serial output
* Parses sensor data
* Prepares sensor data for ROS 2 topics

---

### robot_serial_node

Status: **Tested**

Purpose:

* Reads robot serial messages
* Displays robot behaviour status
* Used during obstacle avoidance and serial communication testing

---

### empwirebot_gui

Status: **Working**

Purpose:

* Provides graphical robot control panel
* Sends movement commands
* Helps test robot movement without only using terminal commands

---

## Planned ROS 2 Packages

### empwirebot_bringup

Status: **Planned**

Purpose:

* Start multiple EmpwireBot nodes together
* Launch motor control
* Launch sensor nodes
* Launch LiDAR node
* Launch camera node
* Future full robot startup launch file

---

### empwirebot_description

Status: **Planned**

Purpose:

* Store robot URDF/Xacro model
* Define robot body
* Define wheels
* Define sensor positions
* Define LiDAR and camera positions
* Support RViz visualisation

---

### empwirebot_control

Status: **Planned**

Purpose:

* Motor control
* `/cmd_vel` handling
* Serial motor communication
* Future velocity tuning

---

### empwirebot_sensors

Status: **Added / Starter Package Created**

Location:

```text
ros2_ws/src/empwirebot_sensors
---
Purpose:
Read ESP32 SENSOR serial data
Parse distance sensor values
Parse AHT10 temperature and humidity
Parse encoder counts
Publish basic ROS 2 topics
Current node:
sensor_serial_node

Current published topics:
/distance/front
/distance/left
/distance/right
/distance/back
/aht10/temperature
/aht10/humidity
/encoder/left
/encoder/right
/esp32/uptime_ms 

Planned future improvements:
Add /imu/data
Add /odom
Improve serial error handling
Add launch file


### empwirebot_lidar

Status: **Planned**

Purpose:

* Add LD06/LD LiDAR support
* Publish `/scan`
* View LiDAR data in RViz
* Prepare SLAM and navigation

---

### empwirebot_camera

Status: **Planned**

Purpose:

* Add Raspberry Pi Camera 8MP support
* Publish camera image topic
* Test image capture
* Prepare future vision and AI features

---

### empwirebot_navigation

Status: **Future**

Purpose:

* Add SLAM
* Add map saving
* Add Nav2 navigation
* Move robot to goals
* Support autonomous navigation

---

## Planned ROS 2 Topics

Future possible topics:

```text
/cmd_vel
/scan
/odom
/tf
/tf_static
/imu/data
/encoder/left
/encoder/right
/distance/front
/distance/left
/distance/right
/distance/back
/aht10/temperature
/aht10/humidity
/camera/image_raw
/camera/camera_info
```

---

## Build Notes

ROS 2 build folders should not be committed to GitHub.

Ignored folders:

```text
build/
install/
log/
```

Build command example:

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

---

## Current Priority

Current ROS 2 priority:

1. Add existing ROS 2 code files to GitHub
2. Improve `empwirebot_sensors`
3. Parse ESP32 `SENSOR` serial output
4. Publish sensor data into ROS 2 topics
5. Add LiDAR `/scan`
6. Add camera support
7. Prepare SLAM and navigation

