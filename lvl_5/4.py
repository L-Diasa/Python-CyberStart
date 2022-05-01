with open("/tmp/randomwordsnumbers.txt", "r") as file:
    data = file.read()

wordNumbers = data.rstrip().split("\n")

with open("/tmp/words.txt", "r") as file:
    data = file.read()
    
array = data.rstrip().split("\n")

newarr = []
 
for number in wordNumbers:
  newarr.append(array[int(number)])

print(" ".join(newarr))
