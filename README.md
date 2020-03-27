# LTG-RC-Car

Project for creating a line following car using a PID AI to control the movement, speed, and steering of RC Car. This project uses the Raspberry Pi Zero with brushed DC motors for both steering and forward movement.
![Car Driving](Images/CarDriving_Trim)

## Hardware Requirements

* Raspberry PI Zero with Raspbian Buster Desktop
* 2 Brushed DC Motors
* (ADD REQUIREMENTS for Hardware)

## Installation (H/S)

### Hardware Installation
Waiting on them from Mohamed.

### Installing the Software
For instructions on how to connect the raspberry pi to your network and install Raspbian Buster, follow these instructions, 
[Setup Raspberry PI](https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows)

To use download and run the scripts within this repo, you must first clone the repo with the command
```
git clone https://github.com/andersonmolter1/LTG-RC-Car-AI/
```
To run the installation script run this chmod command to run the .sh script.
```
chmod u=rwx ./Install 
```
Then run the Install Script with the command where "PI-HostName" is the Hostname of the PI you desire. If let blank it will default to raspberrypi.
```
./Install [PI-HostName]
```
## PID (Proportional-Integral-Derivative) Controller

Control of this car is going to use a PID Controller Model below. "error" will be defined by how far left or right the car is angled relative to the line the car is following. 

![\Large \alpha _{error} = (J_P\vert_{J_{P=25}}error) - (J_D\vert_{J_{D=0=1}}\frac{d}{dt}error) - (J_I\sum_{n=0}^{k\vert_{k=v.len}}v\vert_{v=v[]})](https://latex.codecogs.com/gif.latex?%5Calpha%20_%7Berror%7D%20%3D%20%28J_P%5Cvert_%7BJ_%7BP%3D25%7D%7Derror%29%20-%20%28J_D%5Cvert_%7BJ_%7BD%3D0%3D1%7D%7D%5Cfrac%7Bd%7D%7Bdt%7Derror%29%20-%20%28J_I%5Csum_%7Bn%3D0%7D%5E%7Bk%5Cvert_%7Bk%3Dv.len%7D%7Dv%5Cvert_%7Bv%3Dv%5B%5D%7D%29)

### P (Proportion)
![\Large (J_P\vert_{J_{P=25}}error)](https://latex.codecogs.com/gif.latex?%28J_P%5Cvert_%7BJ_%7BP%3D25%7D%7Derror%29) <br>
This section of the model will be determining the initial amount of steering to be applied depedent on the amount of error off the line the car is experiencing. We will start with this variable at 25 to account for the 4 errors on each side of the line that can occur. 
### I (Integral)
![\Large (J_I\sum_{n=0}^{k\vert_{k=v.len}}v\vert_{v=v[]})](https://latex.codecogs.com/gif.latex?%28J_I%5Csum_%7Bn%3D0%7D%5E%7Bk%5Cvert_%7Bk%3Dv.len%7D%7Dv%5Cvert_%7Bv%3Dv%5B%5D%7D%29) <br>
This section of the model will take into consideration all of the previous errors and add them up. If the summation of these errors is not 0, then this section will smooth out the correction to get back on the line. For now the constant will be set to 1. We will figure out the best value of this constant later.
### D (Derivative)
![\Large (J_D\vert_{J_{D=1}}\frac{d}{dt}error)](https://latex.codecogs.com/gif.latex?%28J_D%5Cvert_%7BJ_%7BD%3D1%7D%7D%5Cfrac%7Bd%7D%7Bdt%7Derror%29) <br>
This portion of the model calculates the delta between the previous error and the current error and then multiply that by the constant which we will figure out in a later step. For now, it will be set to 1. This should reduce the overshoot effect that can happen when the current error greatly deviates from the last error. 
## Authors

* **Anderson Molter** - (https://github.com/andersonmolter1)
* **Mohamed Mohamed**
* **Qin Yang**
* **Sanjay Sarma** - (https://github.com/sanjayovs)
