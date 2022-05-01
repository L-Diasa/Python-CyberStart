import urllib.request

url = "http://127.0.0.1:8082/cookiestore"
y = 5

for i in range(1,75):
  request = urllib.request.Request(url)
  request.add_header("Cookie", "alien_id = "+str(i))
  response = urllib.request.urlopen(request)
  responseStr = str(response.read().decode("utf-8"))
  print(responseStr)
