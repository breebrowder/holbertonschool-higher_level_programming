#!/usr/bin/python3
""" Function that returns the dict description with simple data structure """


def class_to_json(obj):
    """ using dict: a dictionary used to store an objects attributes """
    return obj.__dict__
