import socket
import sys
import os
import re
import time
import traceback
def TCP (car):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = GetServerIP()
    print(ip)
    server_address = (ip, 20000)
    try:
        sock.connect(server_address)
    except Exception as e:
        print(e)
        os._exit(0)
    isConnected = True
    car.isConnected = True
    print("Connected")

    while isConnected:
        data = sock.recv(12, socket.MSG_WAITALL)
        #print(data)
        if not data: break
        car.modifyPID(data)
        try:
            rList = [car.error + 10, car.speed]
            arr = bytearray(rList)
            sock.sendall(arr)
        except BrokenPipeError as e:
            car.isConnected = False
            print("closed")
            sock.close()
            os._exit(0)
    print("exit")
    os._exit(0)
def GetServerIP():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
<<<<<<< HEAD
    # Bind the socket to the port
    server_address = ('', 20005)
    print("heres")

=======
    server_address = ('', 40005)
>>>>>>> fb8657407cee6ebb19b331e2454defd9e0c2d723
    sock.bind(server_address)
    print("heres1")
    data, address = sock.recvfrom(4096)
    print("heres2")
    sock.close()
    return address[0]