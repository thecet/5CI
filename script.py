import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in dirs:
      path = os.path.join(root, name)
