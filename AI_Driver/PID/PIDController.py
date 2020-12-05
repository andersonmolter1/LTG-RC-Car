import RPi.GPIO as GPIO
from time import sleep
import sys
import socket
from datetime import datetime
import MotorControl
from AutoPhat.AutoPhatMD import AutoPhatMD
import re


class PIDController:
    motorDriver = AutoPhatMD()
    socket = 0
    J_P = 25  # Proportion value
    J_I = 0  # Integral Step value
    J_D = 0  # Derivative Step Value
    error = 0  # amount of error on the line the car is experiencing
    isManual = False
    maxSpeed = 100
    pauseCar = False
    PV = 0  # list of all values errors that the car has experienced
    prevError = 0  # error of last calculation used for Derivative calc
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29, GPIO.IN)  # RR IR Sensor
    GPIO.setup(31, GPIO.IN)  # RM IR Sensor
    GPIO.setup(33, GPIO.IN)  # MM IR Sensor
    GPIO.setup(35, GPIO.IN)  # LM IR Sensor
    GPIO.setup(37, GPIO.IN)  # LL IR Sensor

    def Speed(self):  # Gets speed proportional to error term
        return (50 - (abs(self.error) * 8))

    def Proportion(self):  # Calculates P of PID multiplied by the its constant
        return (self.error * self.J_P)

    def Integral(self):  # Calculates I of PID multiplied by the its constant
        return (self.PV * self.J_I)

    def Derivative(self):  # Caluclates D of PID multiplied by the its constant
        return ((self.error - self.prevError) * self.J_D)

    def PID(self):  # Returns PID model
        return abs(self.Proportion() - self.Derivative() - self.Integral())

    def getMotion(self):
        if (self.error > 0):
            tempE = abs(self.error * 63.75)
            self.motorDriver.TurnRight(tempE)
        if (self.error < 0):
            tempE = abs(self.error * 63.75)
            self.motorDriver.TurnLeft(tempE)
    def StopCar(self):
        self.motorDriver.Stop()
    def modifyPID(self, newPID):
        newConstants = re.sub("[^\w]", " ",  newPID).split()
        self.J_P = newConstants[1]
        self.J_I = newConstants[2]
        self.J_D = newConstants[3]
        self.pauseCar = newConstants[4]
        self.isManual = newConstants[5]
        #print(newConstants)

    def driveCar(self):
        line = 1  # if no argument given, will default to line being black with a white background
        noLine = 0
        if (len(sys.argv) > 1 and sys.argv[1] == 2):
            line = 0
            noLine = 1
        while True:
            sleep(0.0075)
            RR = GPIO.input(29)  # Right Right Sensor
            RM = GPIO.input(31)  # Right Middle Sensor
            MM = GPIO.input(33)  # Middle Middle Sensor
            LM = GPIO.input(35)  # Left Middle Sensor
            LL = GPIO.input(37)  # Left Left Sensor
            #print(f'{LL:d} {LM:d} {MM:d} {RM:1d} {RR:d}')
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
                self.motorDriver.Stop()
            elif (LL == noLine and LM == noLine and MM == noLine and RM == noLine and RR == line):
                self.error = 4
                self.getMotion()
            elif (LL == noLine and LM == noLine and MM == noLine and RM == line and RR == line):
                self.error = 3
                self.getMotion()
            elif (LL == noLine and LM == noLine and MM == noLine and RM == line and RR == noLine):
                self.error = 2
                self.getMotion()
            elif (LL == noLine and LM == noLine and MM == line and RM == line and RR == noLine):
                self.error = 1
                self.getMotion()
            elif (LL == noLine and LM == noLine and MM == line and RM == noLine and RR == noLine):
                self.error = 0
                self.getMotion()
            elif (LL == noLine and LM == line and MM == line and RM == noLine and RR == noLine):
                self.error = -1
                self.getMotion()
            elif (LL == noLine and LM == line and MM == noLine and RM == noLine and RR == noLine):
                self.error = -2
                self.getMotion()
            elif (LL == line and LM == line and MM == noLine and RM == noLine and RR == noLine):
                self.error = -3
                self.getMotion()
            elif (LL == line and LM == noLine and MM == noLine and RM == noLine and RR == noLine):
                self.error = -4
                self.getMotion()
            else:
                self.StopCar()
            
