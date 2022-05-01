# Connect over TCP to the following server 'localhost', 10000
# Initiate communication with GET to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#
import re
import socket

import urllib.parse
import urllib.request

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

url = "https://svnweb.freebsd.org/base/head/share/dict/web2?view=co"

req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
data = response.read()
engWords = data.decode('UTF-8').upper().replace("\n", " ")
engWords = ' ' + engWords + ' '

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 10000))
sock.send(b"GET")

encMessages = sock.recv(1024).decode('UTF-8').split('\n')
encMessages.pop(0)
encMessages.pop(3)

decrMessages = []

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for message in encMessages:
  # loop through every possible key
  for key in range(len(LETTERS)):
  # It is important to set translated to the blank string so that the
  # previous iteration's value for translated is clear
      translated = ''

  # The rest of the program is the same as the original Caesar program:

  # run the encryption/decryption code on each symbol in the message
      for symbol in message:
          if symbol in LETTERS:
              num = LETTERS.find(symbol) # get the number of the symbol
              num = num - key

      # handle the wrap-around if num is 26 or larger or less than 0
              if num < 0:
                  num = num + len(LETTERS)

      # add number's symbol at the end of translated
              translated = translated + LETTERS[num]

          else:
      # just add the symbol without encrypting/decrypting
              translated = translated + symbol

      # display the current key being tested, along with its decryption

     #print('Key #%s: %s : ' % (key, translated))
      #print(translated)import re

      translatedWords = translated.split(' ')
      found = True 
      for word in translatedWords:
        if not ((word) in engWords):
          found = False
          break
      if(found):
        decrMessages.append(" ".join(translatedWords))
        
decrMessages = "\n".join(decrMessages)
sock.send(decrMessages.encode())
data = sock.recv(1024)
print(data)
