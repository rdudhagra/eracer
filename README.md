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

## Credits
Built upon the work of these projects:
- [cruise-automation/webviz](https://github.com/cruise-automation/webviz) — debugging webui