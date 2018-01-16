import socket
  
TCP_IP = '127.0.0.1'
TCP_PORT = 5044
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print(bytes(MESSAGE, 'utf-8'))
s.send(bytes(MESSAGE, 'utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)