import os
for root, dirs, files in os.walk("/tmp/aliendir", topdown=False):
   for name in files:
      print(os.path.join(root, name))
