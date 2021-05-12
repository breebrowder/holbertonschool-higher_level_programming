#!/usr/bin/python3
""" function that returns an object represented by a JSON string """

import json


def from_json_string(my_str):
    """ using loads to parse valid JSON str & convert to Py3 data structure """
    return json.loads(my_str)
