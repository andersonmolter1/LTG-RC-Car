import socket
port = 40005
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
print("waiting on port:"+ str(port))
print('here')
data, addr = s.recvfrom(1024)
r