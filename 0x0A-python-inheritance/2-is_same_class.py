#!/usr/bin/python3
""" function that returns True if object is an instance of specified class """


def is_same_class(obj, a_class):
    """ our function """

    if type(obj) is not a_class:
        return False

    return True
