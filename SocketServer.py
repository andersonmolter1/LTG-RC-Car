# DataServer1.py
import sys
from threading import Thread
import socket
import time
import RPi.GPIO as GPIO

VERBOSE = False
IP_PORT = 5000
P_BUTTON = 24 # adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)

def debug(text):
    if VERBOSE:
        print "Debug:---", text
# ---------------------- class SocketHandler ------------------------
class SocketHandler(Thread):
    def __init__(self, conn):
        Thread.__init__(self)
        self.conn = conn

    def run(self):
        global isConnected
        debug("SocketHandler started")
        while True:
            cmd = ""
            try:
                debug("Calling blocking conn.recv()")
                cmd = self.conn.recv(1024)
            except:
                debug("exception in conn.recv()") 
                # happens when connection is reset from the peer
                break
            debug("Received cmd: " + cmd + " len: " + str(len(cmd)))
            if len(cmd) == 0:
                break
            self.executeCommand(cmd)
        conn.close()
        print "Client disconnected. Waiting for next client..."
        isConnected = False
        debug("SocketHandler terminated")

    def executeCommand(self, cmd):
        debug("Calling executeCommand() with  cmd: " + cmd)
        if cmd[:-1] == "go":  # remove trailing "\0"
            if GPIO.input(P_BUTTON) == GPIO.LOW:
                state = "Button pressed"
            else:
                state = "Button released"
            print "Reporting current state:", state
            self.conn.sendall(state + "\0")
# ----------------- End of SocketHandler -----------------------


