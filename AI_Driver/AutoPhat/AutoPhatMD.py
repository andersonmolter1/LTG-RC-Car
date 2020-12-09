from __future__ import print_function
import time
import sys
import math
import qwiic_scmd
import math
# MOTOR 0 STEERING
# MOTOR 1 DRIVE
class AutoPhatMD:
    pastError = 0
    myMotor = qwiic_scmd.QwiicScmd()
    def TurnLeft(self, error):
        if (error > self.pastError):
            for i in range (self.pastError, error, 25):
                self.myMotor.set_drive(0, 1, i)
                self.myMotor.set_drive(1, 0, 255 - i)
            self.pastError = error
            return
        self.myMotor.set_drive(0, 1, error)
        self.myMotor.set_drive(1, 0, 255 - error)
        self.pastError = error
    def TurnRight(self, error):
        if (error > self.pastError):
            for i in range (self.pastError, error, 25):
                self.myMotor.set_drive(0, 1, i)
                self.myMotor.set_drive(1, 0, 255 - i)
            self.pastError = error
            return
        self.myMotor.set_drive(0, 1, error)
        self.myMotor.set_drive(1, 0, 255 - error)
        self.pastError = error
    def Stop(self):
        self.myMotor.set_drive(0, 0, 0)
        self.myMotor.set_drive(1, 0, 0)
    def NoError(self):
        self.myMotor.set_drive(0, 0, 0)
        for i in range (100, 200, 25):
                self.myMotor.set_drive(1, 0, i)
    def __init__(self):
        R_MTR = 0
        L_MTR = 1
        FWD = 0
        BWD = 1
        if self.myMotor.connected == False:
            print("Motor Driver not connected. Check connections.",
                  file=sys.stderr)
            return
        self.myMotor.begin()
        print("Motor initialized.")
        time.sleep(.250)
        # Zero Motor Speeds
        self.myMotor.set_drive(0, 0, 0)
        self.myMotor.set_drive(1, 0, 0)
        self.myMotor.enable()
        print("Motor enabled")