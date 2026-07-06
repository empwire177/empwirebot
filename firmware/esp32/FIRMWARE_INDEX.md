# EmpwireBot ESP32 Firmware Index

This file lists the ESP32 firmware files used in EmpwireBot.

---

## Current Main Firmware

### sensor_serial_v2_1

Location:

```text
firmware/esp32/sensor_serial_v2_1/sensor_serial_v2_1.ino
```

Status: **Current / Active**

Purpose:

* Reads four distance sensors
* Reads AHT10 temperature and humidity sensor
* Reads MPU6050 IMU
* Reads left and right wheel encoders
* Sends sensor data over USB serial
* Prepares data for Raspberry Pi 5 and ROS 2

Serial output format starts with:

```text
SENSOR,
```

Example output fields:

```text
F_MM=
L_MM=
R_MM=
B_MM=
TEMP_C=
HUM_PCT=
MPU_OK=
AX_G=
AY_G=
AZ_G=
GX_DPS=
GY_DPS=
GZ_DPS=
ENC_L=
ENC_R=
UPTIME_MS=
```

---

## Firmware Version Notes

### v2.1

Features:

* Front VL53L1X support
* Left VL53L0X support
* Right VL53L0X support
* Back VL53L0X support
* AHT10 support
* MPU6050 raw I2C support
* Encoder pulse counting
* Serial sensor output

---

## Planned Firmware Files

Future firmware files may include:

### motor_serial_control

Purpose:

* Receive motor commands from Raspberry Pi 5
* Control 4 DC motors through L298N motor drivers
* Support forward, backward, left, right, and stop commands

### encoder_test

Purpose:

* Test left and right wheel encoders individually
* Count pulses
* Calculate pulses per second
* Prepare for odometry

### lidar_serial_test

Purpose:

* Test LD06/LD LiDAR serial data
* Confirm baud rate
* Confirm readable scan data

### imu_test

Purpose:

* Test MPU6050 acceleration and gyro readings
* Check angle output
* Confirm stable IMU data

### tof_test

Purpose:

* Test VL53 distance sensors individually
* Confirm I2C addresses
* Confirm XSHUT pin sequence

---

## Notes

Each firmware file should have:

* Clear version number
* Hardware pin notes
* Required libraries
* Serial output format
* Test status

Do not overwrite working firmware until the new version is tested.

