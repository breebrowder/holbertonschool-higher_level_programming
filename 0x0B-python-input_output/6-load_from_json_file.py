#!/usr/bin/python3
""" Write a function that creates an object from a JSON file """

import json


def load_from_json_file(filename):
    """ using loads to parse a valid JSON string and convert it to Python """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        return json.load(myFile)
