#!/usr/bin/python3
""" function that appends str at the end of txt file (UTF8) &  returns chars """


def append_write(filename="", text=""):
   """ using with statement to simplify management of our files """

   with open(filename, mode="a", encoding="utf-8") as myFile:
        addedchars = myFile.write(text)
        return addedchars
