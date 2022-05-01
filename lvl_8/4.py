import socket
import re

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 10000))

clientsocket.send('any data'.encode())
wordCodes = clientsocket.recv(1024)
wordCodes = wordCodes.decode('UTF-8').rstrip().split("\n")

myfile = open("backdoor.txt", "r")
paragraphs = myfile.read().split("\n\n")

ans = []
pattern = '[!#?,.:";]'

for wordInf in wordCodes:
  wordInf = wordInf.replace(' ', '').split(",")
  parI = int(wordInf[0]) - 1
  paragraph = paragraphs[parI].split("\n")
  lineI = int(wordInf[1]) - 1
  line = paragraph[lineI].split(" ")
  wordI = int(wordInf[2]) - 1
  word = line[wordI]
  word = re.sub(pattern, '', word)
  ans.append(word)
  
ans = "\n".join(ans)

clientsocket.send(ans.encode())
flag = clientsocket.recv(1024)
print(flag)
