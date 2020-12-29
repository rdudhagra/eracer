#!/usr/bin/env bash

cd catkin_ws # ROS stuff
catkin_make # generate build/devel directories
source ./devel/setup.bash # source env variables/etc
cd ..

cd webviz # a webui used to debug ROS systems...used in this repo
npm run bootstrap # install dependencies
npm run build-static-webviz # generate static build in __static_webviz__
cd ..