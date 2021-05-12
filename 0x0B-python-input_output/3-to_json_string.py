#!/usr/bin/python3
""" Function that returns the JSON representation of an object (str) """

import json


def to_json_string(my_obj):
    """ using json to allow for data exchange """

    return json.dumps(my_obj)
