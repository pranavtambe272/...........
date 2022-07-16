import os
import shutil
path=input("Enter the name of the directory to be sorted : ")
File_list=os.listdir(path)

for x in File_list:
    name,ext=os.path.splitext(x)
    ext=ext[1:]
    if ext==' ':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+x,path+'/'+ext+'/'+x)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+x,path+'/'+ext+'/'+x)