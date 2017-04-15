#!/bin/bash

sudo apt-get update
sudo apt-get install -y git python-dev python-setuptools swig

# Download the latest version of wiringPi
pip install wiringpi2

# Test if WiringPi is installed succesfully
python scripts/testinstall.py
