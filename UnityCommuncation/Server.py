import socket #import the socket module

class MySocket:
    def __init__(self):
        s = socket.socket() #Create a socket object
        host = socket.gethostname() #Get the local machine
        port = 5000 # Reserve a port for your service
        s.bind(('', port)) #Bind to the port
        s.listen(5) #Wait for the client connection
    def connect(self, host, port):
        error = '1'
        while True:
            c,addr = s.accept() #Establish a connection with the client
            print("Got connection from" + addr)
            c.send(error)
            c.recv
            c.close()
socket = MySocket()
socket.connect('192.168.1.7', 5000)

# import socket
# class MySocket:
#     def __init__(self, sock=None):
#         if sock is None:
#             self.sock = socket.socket(
#                             socket.AF_INET, socket.SOCK_STREAM)
#         else:
#             self.sock = sock

#     def connect(self, host, port):
#         self.sock.connect((host, port))

#     def mysend(self, msg):
#         totalsent = 0
#         while totalsent < MSGLEN:
#             sent = self.sock.send(msg[totalsent:])
#             if sent == 0:
#                 raise RuntimeError("socket connection broken")
#             totalsent = totalsent + sent

#     def myreceive(self):
#         chunks = []
#         bytes_recd = 0
#         while bytes_recd < MSGLEN:
#             chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
#             if chunk == b'':
#                 raise RuntimeError("socket connection broken")
#             chunks.append(chunk)
#             bytes_recd = bytes_recd + len(chunk)
#         return b''.join(chunks)
# s = MySocket()
# s.connect('192.168.1.7', 5000)
# s.send("hello world")