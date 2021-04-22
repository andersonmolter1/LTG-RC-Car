#!/bin/bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3-pip -y
sudo apt-get install python3-rpi.gpio python3-rpi.gpio -y
sudo pip install sparkfun-qwiic-scmd -y
echo "Enter static IP:"
read static_ip
echo "Enter routers IP:"
read router_ip
echo "interface wlan0\nstatic ip_address=${static_ip}/24" >> /etc/dhcpcd.conf
echo "static routers=${router_ip}" >> /etc/dhcpcd.conf
echo "static domain_name_servers=8.8.8.8 4.4.4.4" >> /etc/dhcpcd.conf 
echo "static domain_search=" >> /etc/dhcpcd.conf
echo "noipv6" >> /etc/dhcpcd.conf
echo "find . -name \".git\" -type d | sed 's/\/.git//' |  xargs -P10 -I{} git -C {} pull" >> .profile
