#!/usr/bin/env bash

# Run this script as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root"
   exit
fi

export DEBIAN_FRONTEND=noninteractive
apt-get install -y python-dev python-pip gcc 
#apt install -y linux-headers-$(uname -r)
pip install evdev pyserial

