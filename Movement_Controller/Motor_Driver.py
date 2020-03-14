import sympy as sym
import  RPi.GPIO as GPIO
from time import sleep
import sys
class Drive:
    J_P = 25 #Proportion value
    J_I = 0 #Integral Step value
    J_D = 0
    error = 0
    PV = [error]
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)
        GPIO.setup(13,GPIO.OUT)
        steering=GPIO.PWM(7,100)
        steering.start(0)
        driving=GPIO.PWM(13,100)
        driving.start(0)
        GPIO.setup(11,GPIO.OUT,initial=1)
        GPIO.setup(12,GPIO.OUT,initial=0)
        GPIO.setup(15,GPIO.OUT,initial=1)
        GPIO.setup(16,GPIO.OUT,initial=0)
        GPIO.setup(29,GPIO.IN) #RR
        GPIO.setup(31,GPIO.IN) #RM
        GPIO.setup(33,GPIO.IN) #MM
        GPIO.setup(35,GPIO.IN) #LM
        GPIO.setup(37,GPIO.IN) #LL
        RR = GPIO.input(29)
        RM = GPIO.input(31)                                                                                    MM = GPIO.input(33)
        LM = GPIO.input(35)                                                                                    LL = GPIO.input(37)
    def offTrack():
        steering.ChangeDutyCycle(0)
        driving.ChangeDutyCycle(0)
    def TurnLeft():
        err = error
        driving.ChangeDutyCycle(50 - (err * 10))
        Gpio.output(11,GPIO.HIGH)
        GPIO.output(12,GPIO.LOW)
        steering.ChangeDutyCycle(25 * err)
    def TurnRight():
        err = error
        driving.ChangeDutyCycle(50 - (err * 10))
        GPIO.output(11,GPIO.LOW)
        GPIO.output(12,GPIO.HIGH)
        steering.ChangeDutyCycle(25 * err)
    def noError():
        err = error
        driving.ChangeDutyCycle(50 - (err * 10))
        steering.ChangeDutyCycle(10)
    def Proportion():
    def Integral():
        SumPV = sum(PV)
    def Derivative():
        
    def driveCar():
        line = 0
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
    
            tempError = 0
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
            PV.append(error)
