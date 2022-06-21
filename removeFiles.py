import time
import shutil
import os
path = "C:\Parth\Schoolwork\Year 8\Year 9 Maths Book"
if os.path.exists(path):
    os.walk(path)
else:
    print("Path does not exist")
days = 5
seconds = time.time()-(days*24*60*60)

ctime = os.stat(path).st_ctime
if seconds > ctime(path):
    os.remove(path)
    print("Removed files")
else:
    print("Done")
return ctime