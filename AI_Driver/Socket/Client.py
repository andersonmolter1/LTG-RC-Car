import socket
import sys
import os
import re
import time
import traceback
def TCP (car):

    # IPList = []
    # for i in range(0, 100):
    #     IPList.append('192.168.1.' + str(i))
    # print(IPList.count)
    # print(IPList[45])
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    ip = GetServerIP()
    print(ip)
    server_address = (ip, 50005)
    print("here")
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
            data = sock.recv(20)
        except socket.timeout as e:
            print(e)
        message = str(car.error)
        newConstants = re.sub("[^\w]", " ",  str(data)).split()
        if (len(newConstants) == 9 and newConstants[1] == 'a') :
            print(newConstants)
            car.modifyPID(newConstants)
        try:
            sock.sendall(str(car.error).encode('utf-8'))
        except BrokenPipeError as e:
            car.isConnected = False
            print("closed")
            sock.close()
            os._exit(0)

def GetServerIP():
        # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the port
    server_address = ('', 40005)
    sock.bind(server_address)
    data, address = sock.recvfrom(4096)
    return address[0]