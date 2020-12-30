# ERacer
![GitHub](https://img.shields.io/github/license/rdudhagra/eracer) [![GitHub issues](https://img.shields.io/github/issues/rdudhagra/eracer)](https://github.com/rdudhagra/eracer/issues)

An open-source self-driving rc car based on ROS and the NVIDIA Jetson Xavier
### Developed by Ravi Dudhagra ([@rdudhagra](github.com/rdudhagra))

## Build Instructions
1. Clone the repo onto the device of your choosing (in this case my NVIDIA Jetson Xavier)
2. Install dependencies:
    - ROS melodic or newer
    - NodeJS >=10.0.0 <12.0.0
    - [librealsense](https://github.com/IntelRealSense/librealsense) 2.0 or newer—install with GPU/Cuda support for best performance, install pyrealsense as well if you want python support
3. `cd` into the `eracer` folder, run `bash init.bash` to setup.

## Running
1. `cd` into the `eracer` folder, run `bash run.bash`, Ctrl+C to stop.
2. Go to `http://[jetson xavier ip]:8080/?rosbridge-websocket-url=ws://[jetson xavier ip]:9090`
3. Import `util/webviz_sample_layout.json` to get started

## Credits
Built upon the work of these projects:
- [@cruise-automation/webviz](https://github.com/cruise-automation/webviz) — debugging webui 
- [@robopeak/rplidar_ros](https://github.com/robopeak/rplidar_ros) — ROS package for the RPLidar A1M8
- [@IntelRealSense/librealsense](https://github.com/IntelRealSense/librealsense) — library for the Intel Realsense D455 camera