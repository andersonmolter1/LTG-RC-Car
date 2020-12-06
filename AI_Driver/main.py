import sys
from _thread import *
import threading
import time
from PID.PIDController import PIDController
import Socket.SocketServer


car = PIDController()


def drive(thread):
    car.driveCar()


def comm(thread):
    Socket.SocketServer.TCP(car)


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
    except Exception as e:
        print(e + "WWWWWWWWWWWWWWWWWWWWWW")
    # both threads completely executed
    print("Done!")
