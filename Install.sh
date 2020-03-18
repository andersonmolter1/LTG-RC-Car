#!/bin/bash
HN = $1 
sudo apt-get update
yes | sudo apt-get dist-upgrade
sudo apt-get install python-rpi.gpio python3-rpi.gpio
sudo apt-get install python3-pip
pip install sympy
y | sudo apt-get install emacs
git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
cd RPi_Cam_Web_Interface
y | ./install.sh
pip install sympy
sudo hostname hN
sudo reboot
