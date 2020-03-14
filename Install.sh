#!/bin/bash
HN = $1 
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install python-rpi.gpio python3-rpi.gpio
sudo service dhcpcd start
sudo systemctl enable dhcpcd
git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
cd RPi_Cam_Web_Interface
./install.sh
sudo hostname hN
sudo reboot
