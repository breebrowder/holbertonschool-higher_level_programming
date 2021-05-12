#!/usr/bin/python3
"""  function that returns True if the object is an instance of a class """


def is_kind_of_class(obj, a_class):
    """ methid that returns true or false """

    if isinstance(obj, a_class) is False:
        return False
    return True
