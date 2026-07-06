# EmpwireBot Pin Map

This file documents the current wiring and pin assignments for EmpwireBot.

## Main Controller

### Raspberry Pi 5

The Raspberry Pi 5 is used as the main computer for:

* ROS 2 Jazzy
* High-level robot control
* Camera processing
* LiDAR processing
* Future SLAM and navigation
* Communication with ESP32 over USB serial

## ESP32 DevKit V1

The ESP32 is used for:

* Motor control
* Sensor reading
* Encoder reading
* Serial communication with Raspberry Pi 5

---

# ESP32 Pin Assignments

## I2C Bus

Used for distance sensors, MPU6050, and AHT10.

| Function | ESP32 Pin |
| -------- | --------- |
| SDA      | GPIO21    |
| SCL      | GPIO22    |

## Distance Sensors

| Sensor | Type                 | Notes                   |
| ------ | -------------------- | ----------------------- |
| Front  | VL53 distance sensor | Front obstacle distance |
| Left   | VL53 distance sensor | Left side distance      |
| Right  | VL53 distance sensor | Right side distance     |
| Back   | VL53 distance sensor | Rear distance           |

## Distance Sensor XSHUT Pins

| Sensor | XSHUT Pin       |
| ------ | --------------- |
| Front  | GPIO12          |
| Left   | GPIO13          |
| Right  | GPIO14          |
| Back   | To be confirmed |

## Wheel Encoders

| Encoder             | ESP32 Pin | Notes          |
| ------------------- | --------- | -------------- |
| Left wheel encoder  | GPIO35    | Input only pin |
| Right wheel encoder | GPIO36    | Input only pin |

Encoder details:

* 20 pulses per wheel rotation
* Wheel diameter: 67.6 mm

## Motor Driver Pins

### Front Left Motor

| Signal | ESP32 Pin |
| ------ | --------- |
| IN1    | GPIO16    |
| IN2    | GPIO17    |
| PWM    | GPIO18    |

### Front Right Motor

| Signal | ESP32 Pin |
| ------ | --------- |
| IN1    | GPIO19    |
| IN2    | GPIO4     |
| PWM    | GPIO5     |

### Rear Left Motor

| Signal | ESP32 Pin |
| ------ | --------- |
| IN1    | GPIO23    |
| IN2    | GPIO25    |
| PWM    | GPIO26    |

### Rear Right Motor

| Signal | ESP32 Pin |
| ------ | --------- |
| IN1    | GPIO27    |
| IN2    | GPIO32    |
| PWM    | GPIO33    |

---

# Other Hardware

## AHT10

Connected to ESP32 I2C bus.

| Signal | ESP32 Pin |
| ------ | --------- |
| SDA    | GPIO21    |
| SCL    | GPIO22    |

## MPU6050

Connected to ESP32 I2C bus.

| Signal | ESP32 Pin |
| ------ | --------- |
| SDA    | GPIO21    |
| SCL    | GPIO22    |

## LD06/LD LiDAR

Status: hardware added, wiring/testing in progress.

| Wire / Signal | Connection      |
| ------------- | --------------- |
| VCC           | To be confirmed |
| GND           | To be confirmed |
| TX            | To be confirmed |
| RX            | To be confirmed |

## Raspberry Pi Camera 8MP

Connected directly to Raspberry Pi 5 camera connector.

---

# Notes

* ESP32 communicates with Raspberry Pi 5 through USB serial.
* ROS 2 runs on Raspberry Pi 5.
* ESP32 handles lower-level motor and sensor tasks.
* This pin map should be updated whenever wiring changes.

