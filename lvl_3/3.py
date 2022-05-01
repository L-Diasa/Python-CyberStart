# CHALLENGE 1: Make a connection to: 127.0.0.1:8080/winning and print
#              the response.
response2 = 
lib.request.urlopen("http://127.0.0.1:8080/winning")
html2 = response2.read()
print(html2)
