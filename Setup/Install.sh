#!/bin/bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3-pip -y
sudo apt-get install python3-rpi.gpio python3-rpi.gpio -y
sudo python3-pip install sparkfun-qwiic-scmd -y
sudo sed -i '/#dtparam=i2c_arm=on/s/^#//g' /boot/config.txt
sudo echo "start_x=1" >> /boot/config.txt
sudo echo "gpu_mem=128" >> /boot/config.txt
sudo service dhcpcd start
sudo systemctl enable dhcpcd
echo "Enter static IP:"
read static_ip
echo "Enter routers IP:"
read router_ip
echo "interface wlan0" >> /etc/dhcpcd.conf
echo "static ip_address=${static_ip}/24" >> /etc/dhcpcd.conf
echo "static routers=${router_ip}" >> /etc/dhcpcd.conf
echo "static domain_name_servers=8.8.8.8 4.4.4.4" >> /etc/dhcpcd.conf 
echo "find . -name \".git\" -type d | sed 's/\/.git//' |  xargs -P10 -I{} git -C {} pull" >> .profile
cd /home/
git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
cd RPi_Cam_Web_Interface
./install.sh --sk
