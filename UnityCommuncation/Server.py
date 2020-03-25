import socket #import the socket module

s = socket.socket() #Create a socket object
host = socket.gethostname() #Get the local machine
port = 12397 # Reserve a port for your service
s.bind(('', port)) #Bind to the port
s.listen(5) #Wait for the client connection
error = '1'
while True:
    c,addr = s.accept() #Establish a connection with the client
    print "Got connection from", addr
    c.send(error)
    c.close()
