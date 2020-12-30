#!/usr/bin/env bash

# kill webviz
kill $(ps aux | grep '[h]ttp-server __static_webviz__' | awk '{print $2}')
