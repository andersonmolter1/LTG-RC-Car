from __future__ import print_function
import time
import sys
import math
import qwiic_scmd
import math
# MOTOR 0 STEERING
# MOTOR 1 DRIVE
class AutoPhatMD:
    TEST= 0
    pastError = 0
    prevSteer = 0
    prevDrive = 0
    myMotor = qwiic_scmd.QwiicScmd()
    def TurnLeft(self, error):
        self.myMotor.set_drive(0, 1, error)
        self.myMotor.set_drive(1, 0, 200 - error)
        time.sleep(0.05)
    def TurnRight(self, error):
        self.myMotor.set_drive(0, 0, error)
        self.myMotor.set_drive(1, 0, 200 - error)
        time.sleep(0.05)
    def Stop(self):
        self.myMotor.set_drive(0, 0, 0)
        time.sleep(0.05)
    def NoError(self):
        self.myMotor.set_drive(0, 0, 0)
        time.sleep(0.05)

    def ManualLeft(self):
        self.myMotor.set_drive(0, 1, 200)
        time.sleep(0.05)
    def ManualRight(self):
        self.myMotor.set_drive(0, 0, 200)
        time.sleep(0.05)
    def ManualSteerStop(self):
        self.myMotor.set_drive(0, 1, 0)
        time.sleep(0.05)
    def ManualForward(self):
        for i in range (125, 150, 1):
            print(i)
            self.myMotor.set_drive(1, 1, i)
            time.sleep(0.01)

            
    def ManualReverse(self):
        for i in range (125, 150, 1):
            print(i)
            self.myMotor.set_drive(1, 0, i)
            time.sleep(0.01)
    def ManualDriveStop(self):
        self.myMotor.set_drive(1, 0, 0)
        time.sleep(0.05)
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