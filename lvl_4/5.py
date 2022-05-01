import socket

# To make a connection to a TCP server:

# Create a socket. AF_INET means you're connecting to an IPv4 IP
#  Address.
# SOCK_STREAM means you are connecting over TCP and not UDP.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tell the socket what IP Address and Port number to connect to.
clientsocket.connect(('localhost', 10000))
# Send some data over the socket.
clientsocket.send('USER'.encode())
data = clientsocket.recv(1024)
print(data)
clientsocket.send('aliensignal'.encode())
data = clientsocket.recv(1024)
print(data)
clientsocket.send('PASS'.encode())
data = clientsocket.recv(1024)
print(data)
clientsocket.send('unlockserver'.encode())
data = clientsocket.recv(1024)
print(data)
clientsocket.send('SEND'.encode())
data = clientsocket.recv(1024)
print(data)
clientsocket.send('moonbase'.encode())
data = clientsocket.recv(1024)
print(data)
clientsocket.send('END'.encode())
data = clientsocket.recv(1024)
print(data)
