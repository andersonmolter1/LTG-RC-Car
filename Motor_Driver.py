import RPi.GPIO as GPIO
from time import sleep
import sys
from datetime import datetime


class DriveAI:
    J_P = 25  # Proportion value
    J_I = 0  # Integral Step value
    J_D = 0  # Derivative Step Value
    error = 0  # amount of error on the line the car is experiencing
    PV = 0  # list of all values errors that the car has experienced
    prevError = 0 # error of last calculation used for Derivative calc
    driving = 0 # driving motor
    steering = 0 # steering motor
    def initialize(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)  # Motor that controls steering
        GPIO.setup(13, GPIO.OUT)  # Motor that controls forward movement
        self.steering = GPIO.PWM(7, 100)
        self.steering.start(0)
        self.driving = GPIO.PWM(13, 100)
        self.driving.start(0)
        GPIO.setup(11, GPIO.OUT, initial=1)  # AIN1
        GPIO.setup(12, GPIO.OUT, initial=0)  # BIN1
        GPIO.setup(15, GPIO.OUT, initial=1)  # AIN2
        GPIO.setup(16, GPIO.OUT, initial=0)  # BIN2
        GPIO.setup(29, GPIO.IN)  # RR IR Sensor
        GPIO.setup(31, GPIO.IN)  # RM IR Sensor
        GPIO.setup(33, GPIO.IN)  # MM IR Sensor
        GPIO.setup(35, GPIO.IN)  # LM IR Sensor
        GPIO.setup(37, GPIO.IN)  # LL IR Sensor
    def setConstants(self, P, I, D):
        self.J_P = P
        self.J_I = I
        self.J_D = D
    def offTrack(self):  # Stops car if it went all the way off track
        self.driving.ChangeDutyCycle(0)
        self.steering.ChangeDutyCycle(0)

    def TurnLeft(self):
        self.prevError = self.error # to calculate derivative in next PID call
        self.PV = self.PV + self.error
        self.error = abs(self.error)
        self.driving.ChangeDutyCycle(self.Speed())
        # flips polarity of motor to change motor direction
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        temp = self.PID() #gets PID Value for later use to steer.
        if (temp > 100): # Defaults to closest valid value if over 100 to not go past GPIO limit of 100 or 0
            temp = 100
        elif (temp < 0):
            temp = 0
        self.steering.ChangeDutyCycle(temp)
        


    def TurnRight(self):
        # Add error to the PV array to calculate I ste
        self.prevError = self.error # to calculate derivative in next PID call
        self.PV = self.PV + self.error
        #self.PV.append(self.error)
        # self.error = abs(self.error)
        self.driving.ChangeDutyCycle(self.Speed())
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        temp = self.PID()
        if (temp > 100):  # Defaults to closest valid value if over 100 to not go past GPIO limit of 100 or 0
            temp = 100
        elif (temp < 0):
            temp = 0
        self.steering.ChangeDutyCycle(temp)
    def noError(self): # if car is going straight then go full speed and move motor to default state.
        self.prevError = self.error # to calculate derivative in next PID call
        self.steering.ChangeDutyCycle(0)
        self.driving.ChangeDutyCycle(50)

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
            print(f'{LL:d} {LM:d} {MM:d} {RM:1d} {RR:d}')
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
                self.offTrack()
            elif (LL == noLine and LM == noLine and MM == noLine and RM == noLine and RR == line):
                self.error = 4
                self.TurnRight()
            elif (LL == noLine and LM == noLine and MM == noLine and RM == line and RR == line):
                self.error = 3
                self.TurnRight()
            elif (LL == noLine and LM == noLine and MM == noLine and RM == line and RR == noLine):
                self.error = 2
                self.TurnRight()
            elif (LL == noLine and LM == noLine and MM == line and RM == line and RR == noLine):
                self.error = 1
                self.TurnRight()
            elif (LL == noLine and LM == noLine and MM == line and RM == noLine and RR == noLine):
                self.noError()
            elif (LL == noLine and LM == line and MM == line and RM == noLine and RR == noLine):
                self.error = -1
                self.TurnLeft()
            elif (LL == noLine and LM == line and MM == noLine and RM == noLine and RR == noLine):
                self.error = -2
                self.TurnLeft()
            elif (LL == line and LM == line and MM == noLine and RM == noLine and RR == noLine):
                self.error = -3
                self.TurnLeft()
            elif (LL == line and LM == noLine and MM == noLine and RM == noLine and RR == noLine):
                self.error = -4
                self.TurnLeft()
            else:
                dump = 0
