# EmpwireBot ESP32 Firmware
## Firmware Index

See the firmware index here:

[Firmware Index](FIRMWARE_INDEX.md)

This folder contains ESP32 firmware used for EmpwireBot motor control, sensor reading, encoder counting, and serial communication with Raspberry Pi 5.

## ESP32 Role

The ESP32 DevKit V1 is used as the low-level controller for EmpwireBot.

It handles:

* Motor driver control
* Distance sensor readings
* MPU6050 IMU readings
* AHT10 temperature and humidity readings
* Wheel encoder pulse counting
* USB serial communication with Raspberry Pi 5

## Communication

The ESP32 communicates with the Raspberry Pi 5 using USB serial.

The Raspberry Pi 5 runs ROS 2 and sends control commands to the ESP32.

The ESP32 sends sensor and system health data back to the Raspberry Pi 5.

## Current Connected Hardware

* 2 x L298N motor drivers
* 4 x TT DC gear motors
* 4 x VL53 distance sensors
* MPU6050 IMU
* AHT10 temperature and humidity sensor
* Left wheel encoder
* Right wheel encoder

## Important Pins

Full pin details are documented here:

[EmpwireBot Pin Map](../../hardware/pin_map.md)

## Current Firmware Stage

Current stage:

**v0.5-dev - LiDAR and Camera Upgrade**

The ESP32 firmware is currently focused on:

* Stable motor control
* Sensor health monitoring
* Encoder reading
* Serial communication with Raspberry Pi 5
* Preparing for ROS 2 sensor integration


## Firmware Files

Current firmware files:

- `sensor_serial_v2_1/sensor_serial_v2_1.ino`
  - Reads four distance sensors
  - Reads AHT10 temperature and humidity
  - Reads MPU6050 IMU
  - Reads left and right wheel encoders
  - Outputs serial `SENSOR` data for Raspberry Pi / ROS 2

Future firmware files may include:

- `motor_serial_control.ino`
- `encoder_test.ino`
- `vl53_test.ino`
- `mpu6050_test.ino`
- `aht10_test.ino`

## Notes

Firmware should be tested individually first before being combined into the main EmpwireBot firmware.

