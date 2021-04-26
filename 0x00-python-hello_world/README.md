## Requirements

### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file at the root of the holbertonschool-higher_level_programming repo, containing a description of the repository
* A README.md file, at the root of the folder of this project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* Shell Scripts
* Allowed editors: vi, vim, emacs
* All your scripts will be tested on Ubuntu 14.04 LTS
* All your scripts should be exactly two lines long (wc -l file should print 2)
* All your files should end with a new line
* The first line of all your files should be exactly #!/bin/bash
* All your files must be executable

### C Scripts
* Allowed editors: vi, vim, emacs
* All your files will be compiled on Ubuntu 14.04 LTS
* Your programs and functions will be compiled with gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic
* All your files should end with a new line
* Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
* You are not allowed to use global variables
* No more than 5 functions per file
* In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you dont have to push them to your r  epo (if you do we wont take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one sh  own in the examples
* The prototypes of all your functions should be included in your header file called lists.h
* Dont forget to push your header file
* All your header files should be include guarded

## Install PEP8
Pycodestyle is now the new standard of Python style code, but at school we will use PEP8, version 1.7.* Dont worry, pycodestyle is based on pep8. The hardest part now is to install it for Python 3:

### Regular Ubuntu 14.04 install
```
$ sudo apt-get install python3-pep8
```
### Using Pip3

### Install Pip3
```
$ sudo apt-get install python3-pip
```
### Install Pep8
```
$ sudo apt-get install python3-pip
```
```
$ sudo pip3 install -Iv pep8==1.7.0
```
-> Make sure you have the right version
```
$ pep8 --version
1.7.0
$
```
Finally, if you cant make it work, please use the container-on-demand tool to PEP8 your files in a pre-configured container.