import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 10000))
clientsocket.send('ls /tmp'.encode())
data = clientsocket.recv(1024)
print(data)
