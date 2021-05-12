#!/usr/bin/python3

""" Function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ using with statement to simplify management of our files """

    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
