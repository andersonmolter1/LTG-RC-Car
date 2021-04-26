import socket
import sys
import os
import re
import time
import traceback
def TCP (car):
    localIP = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    carNum = localIP[len(localIP) - 1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    ip = GetServerIP(carNum)
    print(ip)
    portNumber = '6000' + carNum
    server_address = (ip, int(portNumber))
    try:
        sock.connect(server_address)
    except Exception as e:
        print(e)
        os._exit(0)
    sock.settimeout(3)
    isConnected = True
    car.isConnected = True
    print("Connected")
    # Send data
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
            rList = [car.error + 10, 0]
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
def GetServerIP(carNum):
        # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the port
    print(carNum)
    port = str(carNum) + str("0006")
    server_address = ('', int(port))
    sock.bind(server_address)
    data, address = sock.recvfrom(4096)
    sock.close()
    return address[0]