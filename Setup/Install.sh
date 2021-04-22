#!/bin/bash
sudo apt-get update
yes | sudo apt-get dist-upgrade
yes | sudo apt-get install python-rpi.gpio python3-rpi.gpio -y
yes | sudo apt-get install python3-pip -y
sudo pip install sparkfun-qwiic-scmd -y
sudo apt install git-all -y
echo "find . -name \".git\" -type d | sed 's/\/.git//' |  xargs -P10 -I{} git -C {} pull" >> .profile
