import socket

backlog = 1
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.20', 5000))
s.listen(backlog)
print ("is waiting")
client, address = s.accept()
while 1:
	
	data = client.recv(size)
        if data:
        	print (data)
