#!/usr/bin/python3

import os

dir = os.getcwd() #get current dir

dir_list = os.listdir(dir) # Receiving the list of files in current directory
#dir_list = [f for f in dir_list if os.path.isfile(dir+'/'+f)]

files_list=[] #Files list

extension = input('Input the file extension (you can ignore this option):')
mask = input('Input the end mask (number of ending symbols or delimiter):')

if extension:
    for item in dir_list:
        if item.endswith(extension):
            files_list.append(item)
else:
    files_list=dir_list

#Creating to-be directories list
if mask.isnumeric():
    mask=int(mask)*-1
    for file in files_list:
        name=file.split('.')[0]
        name=name[:mask]
    # Checking if directory exists
    #    if not os.path.exists(dir+'/'+name):
    #        os.makedirs(dir+'/'+name)

        os.makedirs(dir+'/'+name, exist_ok=True)        # A simpler method to check if dir exists
        os.rename(dir+'/'+file, dir+'/'+name+'/'+file)
else:
    for file in files_list:
        if mask in file:
            name=file.split('.')[0]
            name=name.rsplit(mask, 1)
            os.makedirs(dir+'/'+name[0], exist_ok=True)        # A simpler method to check if dir exists
            os.rename(dir+'/'+file, dir+'/'+name[0]+'/'+file)