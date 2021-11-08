import os
import shutil

path = input("enter the diretory you want to clean: ")
day = input("enter the time you want: ")
day = day*86400

if(os.path.exists(path)):
    pathVal = os.walk(path)
    for i in pathVal:
        ctime = os.stat(i).st_ctime
        if(ctime>day):
            name = os.path.split(i)
            if(name[1]==''):
                shutil.rmtree(i)
            else:
                os.remove(i)
else:
    print("path not found")
