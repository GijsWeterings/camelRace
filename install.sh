#!/bin/bash

sudo apt-get install -y git python-dev python-setuptools swig

# Download the latest version of wiringPi
git clone --recursive https://github.com/WiringPi/WiringPi-Python.git wiringPi

# Build the WiringPi dependency
cd wiringPi
git pull origin
./build.sh
cd ..

# Test if WiringPi is installed succesfully
hash gpio -v 2>/dev/null || { echo >&2 "WiringPi was not installed succesfully. Run gpio -v for more information. Aborting."; exit 1; }

