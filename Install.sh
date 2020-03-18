#!/bin/bash
sudo apt-get update
yes | sudo apt-get dist-upgrade
yes | sudo apt-get install python-rpi.gpio python3-rpi.gpio
yes | sudo apt-get install python3-pip
pip install sympy
yes | sudo apt-get install emacs
git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
cd RPi_Cam_Web_Interface
yes | ./install.sh
sudo hostname $1
sudo reboot
