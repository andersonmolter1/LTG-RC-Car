import  RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
m1=GPIO.PWM(11,100)
m1.start(0)
m2=GPIO.PWM(19,100)
m2.start(0)

GPIO.setup(13,GPIO.OUT,initial=1)
GPIO.setup(15,GPIO.OUT,initial=0)
GPIO.setup(21,GPIO.OUT,initial=1)
GPIO.setup(23,GPIO.OUT,initial=0)



for PWMSpd in range(0,101,10):
    print(PWMSpd)
    m1.ChangeDutyCycle(PWMSpd)
    m2.ChangeDutyCycle(PWMSpd)
    sleep(3)
for PWMSpd in range(100,-1,-10):
    m1.ChangeDutyCycle(PWMSpd)
    m2.ChangeDutyCycle(PWMSpd)
    sleep(3)
m1.ChangeDutyCycle(20)
m2.ChangeDutyCycle(0)
sleep(3)
GPIO.output(13,GPIO.LOW)
GPIO.output(15,GPIO.HIGH)

sleep(3)
m1.ChangeDutyCycle(0)
m2.ChangeDutyCycle(20)
sleep(3)
GPIO.output(23,GPIO.HIGH)
GPIO.output(21,GPIO.LOW)
sleep(3)






GPIO.cleanup()
