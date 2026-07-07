import os
from glob import glob

from setuptools import find_packages, setup

package_name = "empwirebot_sensors"

setup(
    name=package_name,
    version="0.5.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py")),
    ],
    install_requires=["setuptools", "pyserial"],
    zip_safe=True,
    maintainer="S M Ashraful Momen",
    maintainer_email="your-email@example.com",
    description="EmpwireBot ROS 2 sensor package for ESP32 serial sensor data.",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "sensor_serial_node = empwirebot_sensors.sensor_serial_node:main",
        ],
    },
)
