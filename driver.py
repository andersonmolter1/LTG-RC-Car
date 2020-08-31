# DataServer1.py
import sys
from threading import Thread
import socket
import time
import RPi.GPIO as GPIO
import Motor_Driver
import SocketServer
car = DriveAI()
car.initialize()
car.driveCar()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# close port when process exits:
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
debug("Socket created")
HOSTNAME = "" # Symbolic name meaning all available interfaces
try:
    serverSocket.bind((HOSTNAME, IP_PORT))
except socket.error as msg:
    print "Bind failed", msg[0], msg[1]
    sys.exit()
serverSocket.listen(10)

print "Waiting for a connecting client..."
isConnected = False
while True:
    debug("Calling blocking accept()...")
    conn, addr = serverSocket.accept()
    print "Connected with client at " + addr[0]
    isConnected = True
    socketHandler = SocketHandler(conn)
    # necessary to terminate it at program termination:
    socketHandler.setDaemon(True)  
    socketHandler.start()
    t = 0
    while isConnected:
        print "Server connected at", t, "s"
	conn.sendall(car.error)
	print(conn.recv(1024))
        time.sleep(.1)