import RPi.GPIO as GPIO
from time import sleep




class MotorControl:
	PWMValue=""
	mf_pwm=""
	mb_pwm=""
	mf_p1=""
	mf_p2=""

	mb_p2=""
	mb_p1=""
	pwmSpeed=""
	def __init__(self):
		self.pwmSpeed=80
		self.pwmSpeed1=80
		self.pwmSpeed2=80
		self.mb_p1=11
		self.mb_p2=12
		self.mf_p1=15
		self.mf_p2=16
		self.PWMValue = 100
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7,GPIO.OUT)
		GPIO.setup(13,GPIO.OUT)
		self.mb_pwm=GPIO.PWM(7,self.PWMValue)
		self.mf_pwm=GPIO.PWM(13,self.PWMValue)
		GPIO.setup(self.mf_p1,GPIO.OUT,initial=0)
		GPIO.setup(self.mf_p2,GPIO.OUT,initial=0) 
		GPIO.setup(self.mb_p1,GPIO.OUT,initial=0) 
		GPIO.setup(self.mb_p2,GPIO.OUT,initial=0) 
		self.mf_pwm.start(0)
		self.mb_pwm.start(0)
	
	def MoveForward(self, driveDegree):
		GPIO.output(self.mb_p1,GPIO.HIGH)
		GPIO.output(self.mb_p2,GPIO.LOW)
		GPIO.output(self.mf_p1,GPIO.LOW)
		GPIO.output(self.mf_p2,GPIO.LOW)
		self.mb_pwm.ChangeDutyCycle(self.pwmSpeed)
	def MoveBackward(self, driveDegree):
		GPIO.output(self.mb_p1,GPIO.LOW)
		GPIO.output(self.mb_p2,GPIO.HIGH)
		GPIO.output(self.mf_p1,GPIO.LOW)
		GPIO.output(self.mf_p1,GPIO.LOW)
		self.mb_pwm.ChangeDutyCycle(self.pwmSpeed)
	def MoveLeft(self, turnDegree):
		#GPIO.output(self.mb_p1,turnDegree)
		#GPIO.output(self.mb_p2,turnDegree)
		GPIO.output(self.mf_p1,turnDegree)
		GPIO.output(self.mf_p2,turnDegree)
		self.mb_pwm.ChangeDutyCycle(self.pwmSpeed2)
		self.mf_pwm.ChangeDutyCycle(self.pwmSpeed1)
	def MoveRight(self, turnDegree):
		#GPIO.output(self.mb_p1,turnDegree)
		#GPIO.output(self.mb_p2,turnDegree)
		GPIO.output(self.mf_p1,turnDegree)
		GPIO.output(self.mf_p2,turnDegree)
		self.mb_pwm.ChangeDutyCycle(self.pwmSpeed2)
		self.mf_pwm.ChangeDutyCycle(self.pwmSpeed1)
	def Stopper(self):
		GPIO.output(self.mb_p1,GPIO.LOW)
		GPIO.output(self.mb_p2,GPIO.LOW)
		GPIO.output(self.mf_p1,GPIO.LOW)
		GPIO.output(self.mf_p2,GPIO.LOW)
		
		self.mf_pwm.ChangeDutyCycle(0)
