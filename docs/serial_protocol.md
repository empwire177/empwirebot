# EmpwireBot Serial Protocol

This document explains the serial communication format used between the ESP32 DevKit V1 and Raspberry Pi 5.

---

## Purpose

EmpwireBot uses USB serial communication between:

* ESP32 DevKit V1
* Raspberry Pi 5

The ESP32 handles low-level hardware.

The Raspberry Pi 5 runs ROS 2 and handles high-level robot control.

---

## Serial Connection

| Item              | Value                                |
| ----------------- | ------------------------------------ |
| Connection type   | USB serial                           |
| ESP32 baud rate   | 115200                               |
| Raspberry Pi side | ROS 2 serial node                    |
| Current direction | ESP32 to Raspberry Pi sensor output  |
| Future direction  | Raspberry Pi to ESP32 motor commands |

---

## Current Sensor Output Format

The current ESP32 sensor firmware outputs one sensor line starting with:

```text
SENSOR,
```

Example format:

```text
SENSOR,F_MM=320,L_MM=450,R_MM=390,B_MM=600,TEMP_C=25.40,HUM_PCT=48.20,MPU_OK=1,AX_G=0.010,AY_G=0.020,AZ_G=1.000,GX_DPS=0.100,GY_DPS=-0.050,GZ_DPS=0.020,MPU_TEMP_C=31.25,ENC_L=120,ENC_R=118,UPTIME_MS=5000
```

---

## Sensor Fields

| Field        | Meaning                      | Unit               |
| ------------ | ---------------------------- | ------------------ |
| `F_MM`       | Front distance sensor        | millimetres        |
| `L_MM`       | Left distance sensor         | millimetres        |
| `R_MM`       | Right distance sensor        | millimetres        |
| `B_MM`       | Back distance sensor         | millimetres        |
| `TEMP_C`     | AHT10 temperature            | Celsius            |
| `HUM_PCT`    | AHT10 humidity               | percent            |
| `MPU_OK`     | MPU6050 read status          | 1 = OK, 0 = error  |
| `AX_G`       | Accelerometer X axis         | g                  |
| `AY_G`       | Accelerometer Y axis         | g                  |
| `AZ_G`       | Accelerometer Z axis         | g                  |
| `GX_DPS`     | Gyroscope X axis             | degrees per second |
| `GY_DPS`     | Gyroscope Y axis             | degrees per second |
| `GZ_DPS`     | Gyroscope Z axis             | degrees per second |
| `MPU_TEMP_C` | MPU6050 internal temperature | Celsius            |
| `ENC_L`      | Left encoder pulse count     | pulses             |
| `ENC_R`      | Right encoder pulse count    | pulses             |
| `UPTIME_MS`  | ESP32 uptime                 | milliseconds       |

---

## Error Values

Distance sensors may return:

```text
-1
```

Meaning:

* Sensor not available
* Out of range
* Read error
* Sensor not initialised

AHT10 may return:

```text
-999.00
```

Meaning:

* AHT10 not detected
* AHT10 read failed

MPU status:

```text
MPU_OK=1
```

means MPU6050 read is OK.

```text
MPU_OK=0
```

means MPU6050 read failed.

---

## Future ROS 2 Topic Mapping

The Raspberry Pi ROS 2 sensor node can parse the serial line and publish data into topics.

Possible future topics:

| Serial Field                 | ROS 2 Topic          |
| ---------------------------- | -------------------- |
| `F_MM`                       | `/distance/front`    |
| `L_MM`                       | `/distance/left`     |
| `R_MM`                       | `/distance/right`    |
| `B_MM`                       | `/distance/back`     |
| `TEMP_C`                     | `/aht10/temperature` |
| `HUM_PCT`                    | `/aht10/humidity`    |
| `AX_G`, `AY_G`, `AZ_G`       | `/imu/data`          |
| `GX_DPS`, `GY_DPS`, `GZ_DPS` | `/imu/data`          |
| `ENC_L`                      | `/encoder/left`      |
| `ENC_R`                      | `/encoder/right`     |
| Encoder calculated odometry  | `/odom`              |

---

## Future Motor Command Format

A future Raspberry Pi to ESP32 motor command format may use simple command lines.

Possible examples:

```text
CMD,STOP
CMD,FWD,120
CMD,BACK,120
CMD,LEFT,100
CMD,RIGHT,100
```

Or future velocity command format:

```text
CMD,LINEAR=0.20,ANGULAR=0.00
CMD,LINEAR=0.00,ANGULAR=0.50
CMD,LINEAR=0.00,ANGULAR=0.00
```

Final motor command format is not confirmed yet.

---

## Recommended Parsing Rules

The ROS 2 serial node should:

1. Read one full line at a time.
2. Check that the line starts with `SENSOR,`.
3. Split the line by commas.
4. Split each field by `=`.
5. Convert numeric values to the correct type.
6. Ignore unknown fields safely.
7. Handle missing fields safely.
8. Treat `-1` distance values as invalid/out-of-range.
9. Treat `MPU_OK=0` as invalid IMU data.
10. Keep running even if one line has a parse error.

---

## Current Firmware Using This Protocol

Current firmware file:

```text
firmware/esp32/sensor_serial_v2_1/sensor_serial_v2_1.ino
```

Current firmware version:

```text
ESP32 Sensor Serial Firmware v2.1
```

---

## Notes

This protocol should stay simple and readable while EmpwireBot is in early development.

If the protocol changes, update this file and the ROS 2 parser together.

