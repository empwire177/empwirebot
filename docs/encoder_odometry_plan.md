# EmpwireBot Encoder Odometry Plan

This document explains the plan for using EmpwireBot wheel encoders to calculate wheel movement, robot distance, speed, and future ROS 2 odometry.

---

## Current Encoder Hardware

EmpwireBot currently has two wheel encoders:

| Encoder             | ESP32 Pin |
| ------------------- | --------- |
| Left wheel encoder  | GPIO35    |
| Right wheel encoder | GPIO36    |

Known encoder details:

* 20 pulses per full wheel rotation
* Wheel diameter: 67.6 mm

---

## Purpose of Encoder Odometry

Wheel encoder odometry will help EmpwireBot estimate:

* Wheel rotation count
* Distance travelled
* Wheel speed
* Robot forward movement
* Robot turning movement
* Future `/odom` topic
* Future SLAM and navigation support

---

## Wheel Calculation

Wheel diameter:

```text
67.6 mm = 0.0676 m
```

Wheel circumference:

```text
circumference = pi * diameter
circumference = 3.14159 * 0.0676
circumference ≈ 0.2124 m
```

This means one full wheel rotation moves the robot about:

```text
0.2124 m
```

Because the encoder gives 20 pulses per wheel rotation:

```text
distance_per_pulse = 0.2124 / 20
distance_per_pulse ≈ 0.01062 m
```

So each encoder pulse is approximately:

```text
10.62 mm
```

---

## Serial Encoder Fields

The ESP32 currently sends encoder values using:

```text
ENC_L
ENC_R
```

Example:

```text
SENSOR,...,ENC_L=120,ENC_R=118,...
```

Where:

| Field   | Meaning                         |
| ------- | ------------------------------- |
| `ENC_L` | Total left encoder pulse count  |
| `ENC_R` | Total right encoder pulse count |

---

## Basic Distance Calculation

For each update:

```text
left_delta = current_left_count - previous_left_count
right_delta = current_right_count - previous_right_count
```

Convert pulse difference to distance:

```text
left_distance = left_delta * distance_per_pulse
right_distance = right_delta * distance_per_pulse
```

Robot centre distance:

```text
center_distance = (left_distance + right_distance) / 2
```

---

## Speed Calculation

Use time difference between updates:

```text
dt = current_time - previous_time
```

Wheel speeds:

```text
left_speed = left_distance / dt
right_speed = right_distance / dt
```

Robot forward speed:

```text
linear_velocity = (left_speed + right_speed) / 2
```

---

## Turning Calculation

To calculate turning accurately, EmpwireBot needs the wheel track width.

Track width means:

```text
distance between left wheel centre and right wheel centre
```

This value still needs to be measured.

Future formula:

```text
angular_velocity = (right_speed - left_speed) / track_width
```

Temporary status:

```text
track_width = to be measured
```

---

## Future ROS 2 Odometry Topic

Planned ROS 2 topic:

```text
/odom
```

Planned message type:

```text
nav_msgs/msg/Odometry
```

The `/odom` topic should include:

* Robot x position
* Robot y position
* Robot heading angle
* Linear velocity
* Angular velocity

---

## First Odometry Implementation Goal

The first version should publish:

* Simple encoder counts
* Distance travelled by each wheel
* Estimated forward distance
* Basic `/odom` message with forward motion

Turning can be improved later after measuring track width.

---

## Required Future Measurement

Measure and document:

```text
wheel_track_width_m = distance between left and right wheel centres
```

This value is required for better turning odometry.

---

## Planned ROS 2 Node Improvements

The `sensor_serial_node` should later add:

* Previous encoder count storage
* Encoder delta calculation
* Time delta calculation
* Distance calculation
* Speed calculation
* `/odom` publisher
* Optional TF transform from `odom` to `base_link`

---

## Related Files

Current ESP32 firmware:

```text
firmware/esp32/sensor_serial_v2_1/sensor_serial_v2_1.ino
```

Current ROS 2 sensor node:

```text
ros2_ws/src/empwirebot_sensors/empwirebot_sensors/sensor_serial_node.py
```

Serial protocol documentation:

```text
docs/serial_protocol.md
```

