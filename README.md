# ERacer
![GitHub](https://img.shields.io/github/license/rdudhagra/eracer) [![GitHub issues](https://img.shields.io/github/issues/rdudhagra/eracer)](https://github.com/rdudhagra/eracer/issues)

An open-source self-driving rc car based on ROS and the NVIDIA Jetson Xavier
### Developed by Ravi Dudhagra ([@rdudhagra](https://github.com/rdudhagra))

## Build Instructions
1. Clone the repo onto the device of your choosing (in this case my NVIDIA Jetson Xavier)
2. Install dependencies:
    - ROS noetic or newer ([Jetson Xavier install](https://github.com/dusty-nv/jetson-containers))
    - [pynmea2](https://github.com/Knio/pynmea2) for parsing GPS data
    - Adafruit IMU libraries [1](https://github.com/adafruit/Adafruit_CircuitPython_FXOS8700) and [2](https://github.com/adafruit/Adafruit_CircuitPython_FXAS21002C)
    - [librealsense](https://github.com/IntelRealSense/librealsense) 2.0 or newer—install with GPU/Cuda support for best performance, install pyrealsense as well if you want python support
    - [IMU Tools](https://github.com/ccny-ros-pkg/imu_tools)
3. `cd` into the `eracer` folder, run `bash init.bash` to setup.

## Running
1. `cd` into the `eracer` folder, run `bash run.bash`, Ctrl+C to stop.
2. Go to `https://webviz.io/app/?rosbridge-websocket-url=ws://[jetson xavier ip]:9090`
3. Import `util/webviz_sample_layout.json` to get started

## Credits
Built upon the work of these projects:
- [@cruise-automation/webviz](https://github.com/cruise-automation/webviz) — debugging webui 
- [@robopeak/rplidar_ros](https://github.com/robopeak/rplidar_ros) — ROS package for the RPLidar A1M8
- [@IntelRealSense/librealsense](https://github.com/IntelRealSense/librealsense) — library for the Intel Realsense D455 camera
- [@Knio/pynmea2](https://github.com/Knio/pynmea2) — python library for parsing NMEA 0183 strings
- [@ccny-ros-pkg/imu_tools](https://github.com/ccny-ros-pkg/imu_tools) — apply madgwick filter on IMU data to get orientation quaternion
- [@dpkoch/imu_calib](https://github.com/dpkoch/imu_calib) — IMU calibration
