# EmpwireBot Camera Setup Notes

This file documents the Raspberry Pi Camera setup progress for EmpwireBot.

---

## Camera Module

Current camera hardware:

* Raspberry Pi Camera 8MP
* Connected to Raspberry Pi 5 camera connector

---

## Purpose of Camera

The camera will help EmpwireBot with:

* Live video preview
* Robot vision
* Object detection experiments
* Visual awareness
* Future AI features
* Future camera-based navigation experiments

---

## Current Status

Status: **Hardware added, testing in progress**

The camera is part of the EmpwireBot v0.5-dev LiDAR and Camera Upgrade stage.

---

## Raspberry Pi 5 Role

The Raspberry Pi 5 handles camera processing.

The ESP32 does not process camera data.

The Raspberry Pi 5 will be responsible for:

* Camera preview
* Image capture
* Video capture
* ROS 2 camera topic publishing
* Future object detection
* Future AI vision tasks

---

## Planned Testing Steps

### Step 1 - Connect Camera

* Turn off Raspberry Pi 5 before connecting the camera
* Connect the camera ribbon cable carefully
* Make sure the ribbon cable is facing the correct direction
* Power on Raspberry Pi 5

### Step 2 - Check Camera Detection

Test whether the Raspberry Pi can detect the camera.

Possible command:

```bash
libcamera-hello --list-cameras
```

### Step 3 - Test Camera Preview

Possible command:

```bash
libcamera-hello
```

### Step 4 - Capture Test Image

Possible command:

```bash
libcamera-jpeg -o test_image.jpg
```

### Step 5 - Capture Test Video

Possible command:

```bash
libcamera-vid -t 5000 -o test_video.h264
```

---

## Future ROS 2 Goals

Planned camera work:

* Add ROS 2 camera support
* Publish camera data into ROS 2
* View camera feed on Raspberry Pi
* Test image processing
* Test object detection
* Add camera documentation
* Prepare future AI vision features

---

## Planned ROS 2 Topics

Future possible topics:

* `/camera/image_raw`
* `/camera/camera_info`

---

## Notes

This document should be updated after the first successful camera detection, image capture, and video test.

