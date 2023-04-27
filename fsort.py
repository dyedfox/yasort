#!/usr/bin/python3

import os

dir = os.getcwd() #get current dir

dir_list = os.listdir(dir) # Receiving the list of files in current directory
#dir_list = [f for f in dir_list if os.path.isfile(dir+'/'+f)]

files_list=[] #Files list
print ('''
>> fsort version 0.1.1 -  fsort is a simple tool for distributing files to folders based on their name prefixes and file extensions.
(https://github.com/dyedfox/fsort)

*Please note: a directory is considered a file with null extension. Be careful while using this option!
''')
extension = input('>> Please enter the file extension (you can leave this option blank if you want to sort all files regardless of their extension): ')
mask = input('>> Please enter the number of ending characters or delimiter to use for sorting files: ')

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
        name=file.rsplit('.', 1)[0][:mask]
    # Checking if directory exists
    #    if not os.path.exists(dir+'/'+name):
    #        os.makedirs(dir+'/'+name)

        os.makedirs(dir+'/'+name, exist_ok=True)        # A simpler method to check if dir exists
        os.rename(dir+'/'+file, dir+'/'+name+'/'+file)
else:
    for file in files_list:
        if mask in file:
            name=file.rsplit('.', 1)[0].rsplit(mask, 1)
            os.makedirs(dir+'/'+name[0], exist_ok=True)        # A simpler method to check if dir exists
            os.rename(dir+'/'+file, dir+'/'+name[0]+'/'+file)