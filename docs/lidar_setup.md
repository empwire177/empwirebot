# EmpwireBot LiDAR Setup Notes

This file documents the LD06/LD LiDAR setup progress for EmpwireBot.

---

## LiDAR Module

Current LiDAR hardware:

* LD06/LD LiDAR
* 4 bare wires
* Planned for ROS 2 mapping and navigation

---

## Purpose of LiDAR

The LiDAR will help EmpwireBot with:

* 360-degree distance scanning
* Obstacle detection
* Mapping
* SLAM
* Autonomous navigation
* Future ROS 2 navigation stack

---

## Current Status

Status: **Hardware added, wiring and testing in progress**

The LiDAR is now part of the EmpwireBot v0.5-dev upgrade stage.

---

## Wiring Notes

The LiDAR has 4 bare wires.

Final wire identification needs to be confirmed before permanent wiring.

| LiDAR Wire / Signal | Connection      | Status  |
| ------------------- | --------------- | ------- |
| VCC                 | To be confirmed | Pending |
| GND                 | To be confirmed | Pending |
| TX                  | To be confirmed | Pending |
| RX                  | To be confirmed | Pending |

---

## Important Safety Notes

* Do not connect LiDAR power until the correct voltage is confirmed.
* Do not guess wire colours without checking the LiDAR documentation or label.
* GND must be shared between LiDAR and the controller.
* TX from LiDAR should go to RX on the controller.
* RX from LiDAR should go to TX on the controller if required.
* ESP32 GPIO34 is input-only, so it can read serial RX but cannot transmit TX.

---

## Planned Testing Steps

### Step 1 - Identify Wires

* Confirm VCC
* Confirm GND
* Confirm TX
* Confirm RX

### Step 2 - Choose Connection Method

Possible options:

* USB to TTL converter
* ESP32 serial bridge
* Direct serial connection to Raspberry Pi using suitable adapter

### Step 3 - First Data Test

* Confirm LiDAR powers on
* Confirm serial data output
* Check baud rate
* Check if scan data is readable

### Step 4 - ROS 2 Integration

* Install or create ROS 2 LiDAR driver
* Publish scan data to `/scan`
* View scan data in RViz
* Prepare for SLAM testing

---

## Future ROS 2 Goals

Planned LiDAR topics:

* `/scan`

Planned use:

* SLAM
* Mapping
* Navigation
* Obstacle avoidance

---

## Notes

This document should be updated after the LiDAR wiring is confirmed and the first successful data test is completed.

