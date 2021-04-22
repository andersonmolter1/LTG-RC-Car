#!/bin/bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3-pip -y
sudo apt-get install python3-rpi.gpio python3-rpi.gpio -y
sudo pip install sparkfun-qwiic-scmd -y
echo "Enter static IP:"
read static_ip
echo "interface wlan0\nstatic ip_address=${static_ip}/24\nstatic routers=192.168.1.1\nstatic domain_name_servers=8.8.8.8 4.4.4.4\nstatic domain_search=\nnoipv6" >> /etc/dhcpcd.conf
echo "find . -name \".git\" -type d | sed 's/\/.git//' |  xargs -P10 -I{} git -C {} pull" >> .profile
