import  RPi.GPIO as GPIO
from time import sleep
import sys

def calibrate():
    print("")
def offTrack():
    steering.ChangeDutyCycle(0)
    driving.ChangeDutyCycle(0)
def turn(error, direction):
    driving.ChangeDutyCycle(50 - (error * 10))
    if (direction == 'l'):
        GPIO.output(11,GPIO.HIGH)
        GPIO.output(12,GPIO.LOW)
    elif (direction == 'r'):
        GPIO.output(11,GPIO.LOW)
        GPIO.output(12,GPIO.HIGH)
    steering.ChangeDutyCycle(25 * error)
def noError(error):
    driving.ChangeDutyCycle(50 - (error * 10))
    steering.ChangeDutyCycle(10)
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
        if (LL == noLine and LM == noLine and MM == noLine and RM == noLine and RR == noLine):
            offTrack()
        elif (LL == noLine and LM == noLine and MM == noLine and RM == noLine and RR == line):
            turn(4, 'r')
        elif (LL == noLine and LM == noLine and MM == noLine and RM == line and RR == line):
            turn(3, 'r')
        elif (LL == noLine and LM == noLine and MM == noLine and RM == line and RR == noLine):
            turn(2, 'r')
        elif (LL == noLine and LM == noLine and MM == line and RM == line and RR == noLine):
            turn(1, 'r')
        elif (LL == noLine and LM == noLine and MM == line and RM == noLine and RR == noLine):
            noError(0)
        elif (LL == noLine and LM == line and MM == line and RM == noLine and RR == noLine):
            turn(1, 'l')
        elif (LL == noLine and LM == line and MM == noLine and RM == noLine and RR == noLine):
            turn(2, 'l')
        elif (LL == line and LM == line and MM == noLine and RM == noLine and RR == noLine):
            turn(3, 'l')
        elif (LL == line and LM == noLine and MM == noLine and RM == noLine and RR == noLine):
            turn(4, 'l')
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
steering=GPIO.PWM(7,100)
steering.start(0)
driving=GPIO.PWM(13,100)
turningSpeed = 25
straightSpeed = 30
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
RM = GPIO.input(31)
MM = GPIO.input(33)
LM = GPIO.input(35)
LL = GPIO.input(37)

driveCar()