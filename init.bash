#!/usr/bin/env bash

cd catkin_ws # ROS stuff
catkin_make # generate build/devel directories
source ./devel/setup.bash # source env variables/etc
cd ..