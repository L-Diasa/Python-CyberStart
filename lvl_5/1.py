def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\\n")

from time import sleep
import socket
myNewfile = open("/tmp/aliensignallog.txt", "w")

debugMsg("All is work...")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 10000))
server_socket.listen(10)

while True:
  connection, address = server_socket.accept()
  data = connection.recv(1024).decode()
  if len(data) > 0:
  	myNewfile.write(data)
  break

server_socket.close()
