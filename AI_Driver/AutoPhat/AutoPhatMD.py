from __future__ import print_function
import time
import sys
import math
import qwiic_scmd
import math
# MOTOR 0 STEERING
# MOTOR 1 DRIVE
class AutoPhatMD:
    myMotor = qwiic_scmd.QwiicScmd()

    def TurnLeft(self, PID):
        self.myMotor.set_drive(0, 0, math.floor(PID))
        self.myMotor.set_drive(1, 0, math.floor(255 - (PID * 63.75)))
    def TurnRight(self, PID):
        self.myMotor.set_drive(0, 1, math.floor(PID) - 1)
        self.myMotor.set_drive(1, 0, math.floor(255 - (PID * 63.75)))
    def Stop(self):
        self.myMotor.set_drive(0, 1, 0)
        self.myMotor.set_drive(1, 0, 0)
    def NoError(self):
        self.myMotor.set_drive(0, 0, 255)
        self.myMotor.set_drive(1, 0, 0)

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
        #self.myMotor.set_drive(1, 0, 0)

        self.myMotor.enable()
        print("Motor enabled")
        # time.sleep(.250)

        # while True:
        #     speed = 20
        #     for speed in range(20, 255):
        #         print(speed)
        #         myMotor.set_drive(R_MTR, FWD, speed)
        #         myMotor.set_drive(L_MTR, BWD, speed)
        #         time.sleep(.05)
        #     for speed in range(254, 20, -1):
        #         print(speed)
        #         myMotor.set_drive(R_MTR, FWD, speed)
        #         myMotor.set_drive(L_MTR, BWD, speed)
        #         time.sleep(.05)

    # if __name__ == '__main__':
    #     try:
    #         runExample()
    #     except (KeyboardInterrupt, SystemExit) as exErr:
    #         print("Ending example.")
    #         myMotor.disable()
    #         sys.exit(0)
