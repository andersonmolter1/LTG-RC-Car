import sys
import socket
import os
import re
import time
import traceback
def TCP (car):
    hostname = socket.gethostname()
    host_addr = socket.gethostbyname(hostname + ".local")
    carNum = 0
    oclet = host_addr.split('.')
    # if (host_addr[-2] != '.'):
    #     carNum = host_addr[-2] + host_addr[-1]
    # else:
    #     carNum = host_addr[-1]
    carNum = oclet[3]
    if (int(carNum) > 99):
        prefPort = '60'
    else:
        prefPort = '600'
    port = int(prefPort + carNum)
    print(port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = GetServerIP(carNum)
    server_address = (ip, port)
    try:
        sock.connect(server_address)
    except Exception as e:
        print(e)
        os._exit(0)
    
    sock.settimeout(3)
    isConnected = True
    car.isConnected = True
    print("Connected")
    while isConnected:
        try:
            data = sock.recv(11, socket.MSG_WAITALL)
        except socket.timeout as e:
            car.isConnected = False
            isConnected = False
            print("closed")
            sock.close()
            os._exit(0)
        if not data: break
        car.modifyPID(data)
        try:
            speed = car.speed
            if (speed < 0):
                speed = 0
            elif (speed > 255):
                speed = 255
            rList = [car.error + 10, speed]
            arr = bytearray(rList)
            sock.sendall(arr)
        except BrokenPipeError as e:
            car.isConnected = False
            isConnected = False
            print("closed")
            sock.close()
            os._exit(0)
    print("exit")
    os._exit(0)
def GetServerIP(deviceNumber):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if (int(deviceNumber) > 99):
        prefPort = '06'
    else:
        prefPort = '006'
    port = int(deviceNumber + prefPort)
    print(port)
    server_address = ('', port)
    sock.bind(server_address)
    data, address = sock.recvfrom(4096)
    sock.close()
    return address[0]
