#found file names by os.walk used for loop for byte reading but then just read all the files to get the flag
#import os
#for root, dirs, files in os.walk("/tmp", topdown=False):
#   for name in files:
#     	print(os.path.join(root, name))   
      
for i in range(0, 20000):     
  with open('/tmp/image-'+ str(i) + '.png', 'rb') as file:
    content = file.read()
    print(str(i) + ":")
    print(content.rstrip())

#byte_s = file.read(8)
#print(str(byte_s) + ' ' + str(i))
