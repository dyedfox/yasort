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

Here is the demo video: https://youtu.be/d_KZdSa7qNA

First, I recommend making an alias for this script in your Linux system:

`alias yasort='python3 /path/to/yasort.py'`, or whatever.

so you can use it as a command in the Terminal.

Example of usage:

```yasort

    >> yasort version 0.4.0 -  yasort (Yet Another Sort Tool) is a simple tool for distributing files to folders based on their name prefixes and file extensions.
    (https://github.com/dyedfox/fsort)

    *Please note: a directory is considered a file with null extension. Be careful while using this option!
    
>> Please enter the file extension (you can leave this option blank if you want to sort all files regardless of their extension): png
>> Please enter the number of ending characters or delimiter to use for sorting files: -
>> Please enter the number of delimiter's position from the end (you can leave this option blank to set it to the default value [1]): 3
The following directories will be created (2 total, existing ones marked with [*]):

[+] My pics 2023-05
[*] My pics 2023-04

Do you want to proceed? (Y/n): 
```


## Acknowledgements
- This project was inspired by GNU/Linux and open-source communities

## Contact
Created by dyedfox - feel free to contact me via GitHub!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
