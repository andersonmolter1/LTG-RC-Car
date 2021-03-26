import sys
from _thread import *
import threading
import time
from PID.PIDController import PIDController
from PID.ModelController import ModelController
import Socket.Client
car = []
# if (sys.argv[1] == 'PID'):
#     car = PIDController()


def drive(thread):
    if (sys.argv[1] == 'ML'):
        print("here")
        car = ModelController()
    car.driveCar()


def comm(thread):
    Socket.Client.TCP(car)


if __name__ == "__main__":
    try:
        # creating thread
        t1 = threading.Thread(target=drive, args=(10,))
        t2 = threading.Thread(target=comm, args=(10,))

        # starting thread 1
        t1.start()
        # starting thread 2
        t2.start()

        # wait until thread 1 is completely executed
        t1.join()
        # wait until thread 2 is completely executed
        t2.join()
        print("here")
    except Exception as e:
        print(e)
        sys.exit()
    # both threads completely executed
    print("Done!")
