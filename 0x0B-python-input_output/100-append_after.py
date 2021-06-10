#!/usr/bin/python3
""" Insert a line of text to a file, after each line containing a spec str """


def append_after(filename="", search_string="", new_string=""):
    """ You must use the with statement """
    """ You don’t need to manage file perm/file don't exist exceptions """
    text = ""
    with open(filename) as myFile:
        for lineoftext in myFile:
            text += lineoftext
            if search_string in lineoftext:
                text += new_string
    with open(filename, mode="w", encoding="utf-8") as w_perm:
        w_perm.write(text)
