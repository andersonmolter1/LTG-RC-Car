import sympy as sym
import  RPi.GPIO as GPIO
from time import sleep
import sys

class DriveAI:
    J_P = 25 # Proportion value
    J_I = 0 # Integral Step value
    J_D = 0 # Derivative Step Value
    error = 0 # amount of error on the line the car is experiencing
    PV = [error] # list of all values errors that the car has experienced
    def __init__(self):
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(7,GPIO.OUT) # Motor that controls steering
        GPIO.setup(13,GPIO.OUT) # Motor that controls forward movement
        steering=GPIO.PWM(7,100)
        steering.start(0)
        driving=GPIO.PWM(13,100)
        driving.start(0)
        GPIO.setup(11,GPIO.OUT,initial=1) #AIN1
        GPIO.setup(12,GPIO.OUT,initial=0) #BIN1
        GPIO.setup(15,GPIO.OUT,initial=1) #AIN2
        GPIO.setup(16,GPIO.OUT,initial=0) #BIN2
        GPIO.setup(29,GPIO.IN) #RR IR Sensor
        GPIO.setup(31,GPIO.IN) #RM IR Sensor
        GPIO.setup(33,GPIO.IN) #MM IR Sensor
        GPIO.setup(35,GPIO.IN) #LM IR Sensor
        GPIO.setup(37,GPIO.IN) #LL IR Sensor
        RR = GPIO.input(29) # Right Right Sensor 
        RM = GPIO.input(31) # Right Middle Sensor
        MM = GPIO.input(33) # Middle Middle Sensor
        LM = GPIO.input(35) # Left Middle Sensor
        LL = GPIO.input(37) # Left Left Sensor
    def offTrack(): # Stops car if it went all the way off track
        steering.ChangeDutyCycle(0)
        drivin.ChangeDutyCycle(0)
    def TurnLeft(): 
        err = error
        driving.ChangeDutyCycle(Speed())
        Gpio.output(11,GPIO.HIGH) # flips polarity of motor to change motor direction
        GPIO.output(12,GPIO.LOW)
        steering.ChangeDutyCycle(PID())
    def TurnRight():
        err = abs(error)
        driving.ChangeDutyCycle(Speed())
        GPIO.output(11,GPIO.LOW)
        GPIO.output(12,GPIO.HIGH)
        steering.ChangeDutyCycle(PID())
    def noError():
        steering.ChangeDutyCycle(0)
        driving.ChangeDutyCycle(50)
    def Speed(): # Gets speed proportional to error term
        return (50  - (abs(error) * 8))
    def Proportion(): # Calculates P of PID
        return (error * J_P)
    def Integral(): # Calculates I of PID
        return sum(PV) 
    def Derivative(): # Caluclates D of PID
        return 0
    def PID(): # Returns PID model
        return (Proportion() - Derivative() - Integral())
    def driveCar(): 
        line = 0 # if no argument given, will default to line being black with a white background
        noLine = 1
        if (len(sys.argv) > 1 and sys.argv[1] == 2):
            line = 1
            noLine = 0
        while True:
            RR = GPIO.input(29)
            RM = GPIO.input(31)
            MM = GPIO.input(33)
            LM = GPIO.input(35)
            LL = GPIO.input(37)
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
                offTrack()
            elif (LL == noLine and LM == noLine and MM == noLine and RM == noLine and RR == line):
                error = 4
                TurnRight()
            elif (LL == noLine and LM == noLine and MM == noLine and RM == line and RR == line):
                error = 3
                TurnRight()
            elif (LL == noLine and LM == noLine and MM == noLine and RM == line and RR == noLine):
                error = 2
                TurnRight()
            elif (LL == noLine and LM == noLine and MM == line and RM == line and RR == noLine):
                error = 1
                TurnRight()
            elif (LL == noLine and LM == noLine and MM == line and RM == noLine and RR == noLine):
                noError(0)
            elif (LL == noLine and LM == line and MM == line and RM == noLine and RR == noLine):
                error = -1
                TurnLeft()
            elif (LL == noLine and LM == line and MM == noLine and RM == noLine and RR == noLine):
                error = -2
                TurnLeft()
            elif (LL == line and LM == line and MM == noLine and RM == noLine and RR == noLine):
                error = -3
                TurnLeft()
            elif (LL == line and LM == noLine and MM == noLine and RM == noLine and RR == noLine):
                error = -4
                TurnLeft()
            PV.append(error) # Adds error to PV list for intgeral calculation
            
