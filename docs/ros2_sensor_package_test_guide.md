# EmpwireBot ROS 2 Sensor Package Test Guide

This guide explains how to build and test the `empwirebot_sensors` ROS 2 package on Raspberry Pi 5.

---

## Purpose

The `empwirebot_sensors` package reads ESP32 serial sensor data and publishes it into ROS 2 topics.

Current supported data:

* Front distance sensor
* Left distance sensor
* Right distance sensor
* Back distance sensor
* AHT10 temperature
* AHT10 humidity
* Left wheel encoder count
* Right wheel encoder count
* ESP32 uptime
* MPU6050 IMU data
* Basic encoder odometry

---

## Current ROS 2 Package

Package name:

```text
empwirebot_sensors
```

Current node:

```text
sensor_serial_node
```

Launch file:

```text
sensor_serial.launch.py
```

---

## Expected ESP32 Serial Format

The ESP32 should send lines like this:

```text
SENSOR,F_MM=320,L_MM=450,R_MM=390,B_MM=600,TEMP_C=25.40,HUM_PCT=48.20,MPU_OK=1,AX_G=0.010,AY_G=0.020,AZ_G=1.000,GX_DPS=0.100,GY_DPS=-0.050,GZ_DPS=0.020,ENC_L=120,ENC_R=118,UPTIME_MS=5000
```

The node ignores lines that do not start with:

```text
SENSOR,
```

---

## Step 1 - Copy Repository to Raspberry Pi

On Raspberry Pi 5, clone the repository if it is not already there:

```bash
git clone https://github.com/empwire177/empwirebot.git
```

Enter the project:

```bash
cd empwirebot
```

---

## Step 2 - Check ROS 2 Environment

Source ROS 2 Jazzy:

```bash
source /opt/ros/jazzy/setup.bash
```

Check ROS 2:

```bash
ros2 --version
```

---

## Step 3 - Install Python Serial Support

Install serial support if needed:

```bash
sudo apt update
sudo apt install python3-serial
```

---

## Step 4 - Build the Package

Go to the ROS 2 workspace:

```bash
cd ~/empwirebot/ros2_ws
```

Build only the sensor package:

```bash
colcon build --packages-select empwirebot_sensors
```

Source the workspace:

```bash
source install/setup.bash
```

---

## Step 5 - Find ESP32 Serial Port

Connect the ESP32 to Raspberry Pi using USB.

Check serial devices:

```bash
ls /dev/ttyUSB*
```

Possible ports:

```text
/dev/ttyUSB0
/dev/ttyUSB1
```

Sometimes ESP32 may appear as:

```bash
ls /dev/ttyACM*
```

Possible port:

```text
/dev/ttyACM0
```

---

## Step 6 - Run the Sensor Node

Default command:

```bash
ros2 run empwirebot_sensors sensor_serial_node
```

With custom port:

```bash
ros2 run empwirebot_sensors sensor_serial_node --ros-args -p port:=/dev/ttyUSB0
```

---

## Step 7 - Run Using Launch File

Default launch command:

```bash
ros2 launch empwirebot_sensors sensor_serial.launch.py
```

With custom port:

```bash
ros2 launch empwirebot_sensors sensor_serial.launch.py port:=/dev/ttyUSB0
```

With custom port and baud rate:

```bash
ros2 launch empwirebot_sensors sensor_serial.launch.py port:=/dev/ttyUSB0 baudrate:=115200
```

---

## Step 8 - Check ROS 2 Topics

Open a new terminal.

Source ROS 2 and the workspace:

```bash
source /opt/ros/jazzy/setup.bash
cd ~/empwirebot/ros2_ws
source install/setup.bash
```

List topics:

```bash
ros2 topic list
```

Expected topics:

```text
/distance/front
/distance/left
/distance/right
/distance/back
/aht10/temperature
/aht10/humidity
/encoder/left
/encoder/right
/esp32/uptime_ms
/imu/data
/odom
```

---

## Step 9 - Echo Sensor Topics

Front distance:

```bash
ros2 topic echo /distance/front
```

Temperature:

```bash
ros2 topic echo /aht10/temperature
```

Humidity:

```bash
ros2 topic echo /aht10/humidity
```

Left encoder:

```bash
ros2 topic echo /encoder/left
```

Right encoder:

```bash
ros2 topic echo /encoder/right
```

IMU data:

```bash
ros2 topic echo /imu/data
```

Odometry:

```bash
ros2 topic echo /odom
```

---

## Step 10 - Check Topic Rates

Check front distance rate:

```bash
ros2 topic hz /distance/front
```

Check IMU rate:

```bash
ros2 topic hz /imu/data
```

Check odometry rate:

```bash
ros2 topic hz /odom
```

---

## Step 11 - Common Problems

### Problem: ESP32 port not found

Check USB connection:

```bash
lsusb
```

Check serial devices:

```bash
ls /dev/ttyUSB*
ls /dev/ttyACM*
```

---

### Problem: Permission denied on serial port

Add user to dialout group:

```bash
sudo usermod -a -G dialout $USER
```

Then reboot:

```bash
sudo reboot
```

---

### Problem: Node starts but no topics update

Check ESP32 serial output in Arduino Serial Monitor first.

Make sure ESP32 sends lines starting with:

```text
SENSOR,
```

---

### Problem: Parse errors

Possible causes:

* ESP32 output format changed
* Missing commas
* Missing equals signs
* Non-numeric values
* Serial baud rate mismatch

---

## Current Limitations

Current `/odom` limitation:

* Encoders currently count pulses only
* Direction is not confirmed from encoder signal
* Wheel track width is not measured yet
* Turning odometry is basic until `wheel_track_width_m` is set

Future improvement:

* Add wheel direction support
* Add better odometry
* Add TF transform
* Improve IMU filtering

---

## Related Files

ROS 2 package:

```text
ros2_ws/src/empwirebot_sensors
```

Sensor node:

```text
ros2_ws/src/empwirebot_sensors/empwirebot_sensors/sensor_serial_node.py
```

Launch file:

```text
ros2_ws/src/empwirebot_sensors/launch/sensor_serial.launch.py
```

Serial protocol:

```text
docs/serial_protocol.md
```

Encoder odometry plan:

```text
docs/encoder_odometry_plan.md
```

