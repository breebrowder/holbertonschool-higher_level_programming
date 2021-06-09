#!/usr/bin/python3
""" Module: LockedClass is our class """


class LockedClass:
    """ Write class that prevents user from dynamically creating new inst """
    __slots__ = "first_name"
