# One of the agents has intercepted a file from the aliens
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif
#
ch1 = open("/tmp/destroymoonbase.gif", "r+")
ch2 = ch1.read()

ch2 = str(ch2).replace("#","")
ch2 = str(ch2).replace("$","")
print(ch2)
