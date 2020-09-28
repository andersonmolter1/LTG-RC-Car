import sys
from threading import Thread
import time
import PIDController
import SocketServer
import _thread

car = PIDController()
def drive(thread):
    car.driveCar()
def comm(thread):
    SocketServer.TCP(car)
try:
    _thread.start_new_thread( drive ,( 1,))
    _thread.start_new_thread( comm ,( 1,))
except:
    print(Exception)
while 1:
   pass
