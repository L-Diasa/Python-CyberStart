import socket
import gzip
from io import BytesIO

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 10000))

sock.send(b"GET_KEY")
data = sock.recv(4096)
print(data)

fil = gzip.GzipFile(fileobj = BytesIO(data), mode ='rb')
print(fil.read())
