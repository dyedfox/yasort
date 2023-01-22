#!/usr/bin/python3

import os

dir = os.getcwd() #get current dir

dir_list = os.listdir(dir) # Receiving the list of files in current directory
#dir_list = [f for f in dir_list if os.path.isfile(dir+'/'+f)]

jpegs=[] #For jpeg files only

mask = input('Input end mask (-x):')

for item in dir_list:
    if item.endswith('.jpg') or item.endswith('.jpeg'):
        jpegs.append(item)

#Creating to-be directories list

if mask.isnumeric():
    mask=int(mask)*-1
    for file in jpegs:
        name=file.split('.')[0]
        name=name[:mask]
    # Checking if directory exists
    #    if not os.path.exists(dir+'/'+name):
    #        os.makedirs(dir+'/'+name)

        os.makedirs(dir+'/'+name, exist_ok=True)        # A simpler method to check if dir exists
        os.rename(dir+'/'+file, dir+'/'+name+'/'+file)
else:
    for file in jpegs:
        name=file.split('.')[0]
        name=name.rsplit(mask, 1)
        os.makedirs(dir+'/'+name[0], exist_ok=True)        # A simpler method to check if dir exists
        os.rename(dir+'/'+file, dir+'/'+name[0]+'/'+file)