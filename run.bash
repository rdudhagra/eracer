#!/usr/bin/env bash

sudo chmod 666 /dev/ttyUSB0 #rplidar permissions
sudo chmod 666 /dev/ttyTHS0 #gps permissions

mkdir -p logs

cd catkin_ws # ROS stuff
catkin_make # generate build/devel directories
source ./devel/setup.bash # source env variables/etc
roslaunch eracer main.launch | tee ../logs/ROS.log # launch eracer ROS
cd ..

# cleanup
kill $(jobs -p)
echo "ERacer: All processes stopped."