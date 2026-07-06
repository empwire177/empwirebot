# EmpwireBot Current Hardware List

## Main Controllers
- Raspberry Pi 5
- ESP32 DevKit V1

## Drive System
- 4-wheel robot chassis
- 4 x TT DC gear motors
- 2 x L298N motor drivers
- Wheel encoders
  - Left encoder: ESP32 GPIO35
  - Right encoder: ESP32 GPIO36
  - 20 pulses per wheel rotation
  - Wheel diameter: 67.6 mm

## Sensors
- 4 x VL53 distance sensors
  - Front distance sensor
  - Left distance sensor
  - Right distance sensor
  - Back distance sensor
- MPU6050 IMU
- AHT10 temperature and humidity sensor
- LD06/LD LiDAR
- Raspberry Pi Camera 8MP

## Communication
- ESP32 connected to Raspberry Pi 5 using USB serial
- ROS 2 running on Raspberry Pi 5
- ESP32 handles motor/sensor side
- Raspberry Pi 5 handles ROS 2, control, camera, LiDAR, and higher-level logic

## Current Project Stage
EmpwireBot is currently in the sensor expansion and GitHub documentation stage.
