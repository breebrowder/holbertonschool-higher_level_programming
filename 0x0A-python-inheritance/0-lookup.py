#!/usr/bin/python3
""" function that returns list of avail attributes & methods of an object """


def lookup(obj):
    """ returns a list object """
    return(dir(obj))
