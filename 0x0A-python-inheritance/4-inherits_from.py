#!/usr/bin/python3
""" function that returns True if the object is an instance inherited """


def inherits_from(obj, a_class):
    """ method that will return """

    if isinstance(obj, a_class) is False:
        return False

    elif type(obj) is a_class:
        return False

    return True
