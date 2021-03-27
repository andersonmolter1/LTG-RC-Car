import RPi.GPIO as GPIO
from time import sleep
import sys
import socket
from datetime import datetime
from AutoPhat.AutoPhatMD import AutoPhatMD
import os


class ModelController:
    isConnected = False
    motorDriver = AutoPhatMD()
    steeringM = 0
    drivingM = 0
    speed = 0
    socket = 0
    error = 0  # amount of error on the line the car is experiencing
    isManual = 0
    maxSpeed = 100
    pauseCar = False
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29, GPIO.IN)  # RR IR Sensor
    GPIO.setup(31, GPIO.IN)  # RM IR Sensor
    GPIO.setup(33, GPIO.IN)  # MM IR Sensor
    GPIO.setup(35, GPIO.IN)  # LM IR Sensor
    GPIO.setup(37, GPIO.IN)  # LL IR Sensor

    def Speed(self):  # Gets speed proportional to error term
        return (200 - (abs(self.error) * 8))

    def getMotion(self):
        if (self.error == -5):
            self.motorDriver.Stop()
        if (self.error == 0):
            self.motorDriver.NoError()
        if (self.error > 0):
            tempE = abs(self.error * 40)
            self.motorDriver.TurnRight(tempE)
        if (self.error < 0):
            tempE = abs(self.error * 40)
            self.motorDriver.TurnLeft(tempE)

    def modifyPID(self, newConstants):
        self.turningDegree = newConstants[0]
        self.drivingDegree = newConstants[1]
        self.pauseCar = newConstants[2]
        self.isManual = newConstants[3]
        self.steeringM = newConstants[4]
        self.drivingM = newConstants[5]
    def DisconnectCar(self):
        self.motorDriver.Stop()
        os._exit(0)
    def driveCar(self):
        line = 1  # if no argument given, will default to line being black with a white background
        noLine = 0
        if (len(sys.argv) > 1 and sys.argv[1] == 2):
            line = 0
            noLine = 1
        while (True):
            if (self.isConnected):
                if (self.isManual == 1):
                    if (self.steeringM == 2):
                        self.motorDriver.myMotor.enable()
                        self.motorDriver.ManualLeft()
                    if (self.steeringM == 1): 
                        self.motorDriver.myMotor.enable()
                        self.motorDriver.ManualRight()
                    if (self.steeringM == 0):
                        self.motorDriver.myMotor.disable()
                    if (self.drivingM == 1):
                        self.motorDriver.myMotor.enable()
                        self.motorDriver.ManualForward()
                    if (self.drivingM == 2):
                        self.motorDriver.myMotor.enable()
                        self.motorDriver.ManualReverse()
                    if (self.drivingM == 0):
                        self.motorDriver.myMotor.disable()
                        self.motorDriver.ManualDriveStop()
                else:
                    RR = GPIO.input(29)  # Right Right Sensor
                    RM = GPIO.input(31)  # Right Middle Sensor
                    MM = GPIO.input(33)  # Middle Middle Sensor
                    LM = GPIO.input(35)  # Left Middle Sensor
                    LL = GPIO.input(37)  # Left Left Sensor
                    # 0 0 0 0 1 ==> Error = 4
                    # 0 0 0 1 1 ==> Error = 3
                    # 0 0 0 1 0 ==> Error = 2
                    # 0 0 1 1 0 ==> Error = 1
                    # 0 0 1 0 0 ==> Error = 0
                    # 0 1 1 0 0 ==> Error = -1
                    # 0 1 0 0 0 ==> Error = -2
                    # 1 1 0 0 0 ==> Error = -3
                    # 1 0 0 0 0 ==> Error = -4
                    if (LL == noLine and LM == noLine and MM == noLine and RM == noLine and RR == noLine):
                        self.error = -5
                    elif (LL == noLine and LM == noLine and MM == noLine and RM == noLine and RR == line):
                        self.error = 4
                    elif (LL == noLine and LM == noLine and MM == noLine and RM == line and RR == line):
                        self.error = 3
                    elif (LL == noLine and LM == noLine and MM == noLine and RM == line and RR == noLine):
                        self.error = 2
                    elif (LL == noLine and LM == noLine and MM == line and RM == line and RR == noLine):
                        self.error = 1
                    elif (LL == noLine and LM == noLine and MM == line and RM == noLine and RR == noLine):
                        self.error = 0
                    elif (LL == noLine and LM == line and MM == line and RM == noLine and RR == noLine):
                        self.error = -1
                    elif (LL == noLine and LM == line and MM == noLine and RM == noLine and RR == noLine):
                        self.error = -2
                    elif (LL == line and LM == line and MM == noLine and RM == noLine and RR == noLine):
                        self.error = -3
                    elif (LL == line and LM == noLine and MM == noLine and RM == noLine and RR == noLine):
                        self.error = -4
                    else:
                        self.error = -5