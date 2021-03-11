import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('', 40005)
sock.bind(server_address)
print (str(sys.stderr) +  '\nwaiting to receive message')
data, address = sock.recvfrom(4096)
print (data + str(address))