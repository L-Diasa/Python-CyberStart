import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 10000))

clientsocket.send('GET_KEY'.encode())
stringReversed = (clientsocket.recv(1024))[::-1]

clientsocket.send(stringReversed)
response = clientsocket.recv(1024)
print(response)

