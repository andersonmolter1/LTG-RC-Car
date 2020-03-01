import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT,initial=0)
GPIO.output(3,1)
GPIO.setup(11,GPIO.OUT,initial=1)
GPIO.output(11,1)
GPIO.setup(13,GPIO.OUT,initial=1)
GPIO.output(13,1)

GPIO.setup(15,GPIO.OUT,initial=0)
GPIO.output(15,0)
sleep(5)
