# CHALLENGE 1: Write a for loop that will create a file called
#              /tmp/cars.txt. There should be 50 lines of text in the
#              file. The first line should be "There are 0 cars"
#              and 1 car should be added every line. Until
#              the last line which should read "There are 49 cars"
myfile = open("/tmp/cars.txt", "w")
for x in range(50):
  myfile.write("There are %d cars\n" % x)

# CHALLENGE 2: Open the file at /tmp/cars.txt and read the contents.
#              Print the contents to the screen.
with open("/tmp/cars.txt", "r") as myfile:
    print(myfile.read())
