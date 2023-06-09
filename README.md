# yasort
> A simple way of distributing files to directories based on their name prefixes and file extension.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- How does this script work? For example, a set of files `[gallery1_001.jpg .. gallery1_119.jpg, gallery2_001.jpg .. gallery2_227.jpg]` 
will be distributed into directories `[gallery1, gallery2]` respectively.
- This script simply makes life a little easier :)

<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Technologies Used
- Python 3.10 + os module from the Python Standart Library

## Features
- An option to split files by their extensions
- Posibility to choose a delimiter and its position from the end

## Usage

<!-- Here is the demo video: https://youtu.be/d_KZdSa7qNA -->

First, I recommend making an alias for this script in your Linux system:

`alias yasort='python3 /path/to/yasort.py'`, or whatever.

so you can use it as a command in the Terminal.

Example 1 of usage:

```dyedfox@my-pc:~/dir$ yasort

yasort version 0.9.0 -  yasort (Yet Another Sort Tool) is a simple tool for distributing files to folders based on their name prefixes and file extensions.
(https://github.com/dyedfox/yasort)

*Please note: a directory is considered a file with null extension. Be careful while using this option!
    
>> Please enter the file extension (you can leave this option blank if you want to sort all files regardless of their extension): 
>> Please enter the number of ending characters or delimiter to use for sorting files: 3
The following directories will be created (3 total, existing ones marked with [*]):

[*] 187
[*] 188
[*] 189

Do you want to proceed? (Y/n): 

File '/home/yaroslav/tmp2/188/188009.txt' already exists. Do you want to overwrite it? (y/N): 
188009.txt skipped.
189001.txt -> /home/yaroslav/tmp2/189/189001.txt
189002.txt -> /home/yaroslav/tmp2/189/189002.txt

File '/home/yaroslav/tmp2/189/189003.txt' already exists. Do you want to overwrite it? (y/N): y
189003.txt -> /home/yaroslav/tmp2/189/189003.txt
187001.txt -> /home/yaroslav/tmp2/187/187001.txt

File '/home/yaroslav/tmp2/187/187002.txt' already exists. Do you want to overwrite it? (y/N): y
187002.txt -> /home/yaroslav/tmp2/187/187002.txt
187003.txt -> /home/yaroslav/tmp2/187/187003.txt
188004.txt -> /home/yaroslav/tmp2/188/188004.txt
188008.txt -> /home/yaroslav/tmp2/188/188008.txt

Operation completed. 9 file(s) total, 1 file(s) skipped, 2 file(s) overwritten.```

Example 2 of usage:

```dyedfox@my-pc:~/dir$ yasort

yasort version 0.9.0 -  yasort (Yet Another Sort Tool) is a simple tool for distributing files to folders based on their name prefixes and file extensions.
(https://github.com/dyedfox/yasort)

*Please note: a directory is considered a file with null extension. Be careful while using this option!
    
>> Please enter the file extension (you can leave this option blank if you want to sort all files regardless of their extension): txt
>> Please enter the number of ending characters or delimiter to use for sorting files: _
>> Please enter the number of delimiter's position from the end (you can leave this option blank to set it to the default value [1]): 1
The following directories will be created (3 total, existing ones marked with [*]):

[+] 187
[*] 188
[*] 189

Do you want to proceed? (Y/n): 
187_001.txt -> /home/yaroslav/tmp2/187/187_001.txt
187_002.txt -> /home/yaroslav/tmp2/187/187_002.txt
187_003.txt -> /home/yaroslav/tmp2/187/187_003.txt

File '/home/yaroslav/tmp2/188/188_001.txt' already exists. Do you want to overwrite it? (y/N): y
188_001.txt -> /home/yaroslav/tmp2/188/188_001.txt

File '/home/yaroslav/tmp2/188/188_002.txt' already exists. Do you want to overwrite it? (y/N): y
188_002.txt -> /home/yaroslav/tmp2/188/188_002.txt
188_003.txt -> /home/yaroslav/tmp2/188/188_003.txt
189_001.txt -> /home/yaroslav/tmp2/189/189_001.txt

File '/home/yaroslav/tmp2/189/189_002.txt' already exists. Do you want to overwrite it? (y/N): n
189_002.txt skipped.
189_003.txt -> /home/yaroslav/tmp2/189/189_003.txt

Operation completed. 9 file(s) total, 1 file(s) skipped, 2 file(s) overwritten.

```

## Acknowledgements
- This project was inspired by GNU/Linux and open-source communities

## Contact
Created by dyedfox - feel free to contact me via GitHub!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
