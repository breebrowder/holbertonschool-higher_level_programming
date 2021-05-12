#!/usr/bin/python3
""" Function that writes a string to a text file (UTF8) and returns chars """


def write_file(filename="", text=""):
    """ using with statement to simplify management of our files """

    with open(filename, mode="w", encoding="utf-8") as myFile:
        characters = myFile.write(text)
        return characters
