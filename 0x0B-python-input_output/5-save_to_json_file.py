#!/usr/bin/python3
""" Function that writes object to a text file, using a JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """ using dump to store python objects in a file """

    with open(filename, mode="w", encoding="utf-8") as myFile:
        return json.dump(my_obj, myFile)
