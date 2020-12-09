import socket
import sys
import os
import time
import traceback
def TCP (car):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('192.168.1.3', 50005)
    try:
        sock.connect(server_address)
    except Exception as e:
        print(e)
        os._exit(0)
    
    isConnected = True
    car.isConnected = True
    print("Connected")
    # Send data
    while isConnected:
        try:
            data = sock.recv(50)
        except socket.timeout as e:
            print(e)
        message = str(car.error)
        car.modifyPID(str(data))
        try:
            sock.sendall(str(car.error).encode('utf-8'))
        except BrokenPipeError as e:
            car.isConnected = False
            print("closed")
            sock.close()
            os._exit(0)
    