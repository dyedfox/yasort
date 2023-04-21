# fsort
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
- Posibility to choose a delimiter

## Usage

First, I recommend making an alias for this script in your Linux system:

`alias fsort='python3 /path/to/fsort.py'`, or whatever.

so you can use it as a command in the Terminal.

Example of usage:

`fsort`\
`Input file extension (you can ignore this option):`\
`Input end mask (number of ending symbols or delimiter):_`

## Acknowledgements
- This project was inspired by GNU/Linux and open-source communities

## Contact
Created by dyedfox - feel free to contact me via GitHub!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
