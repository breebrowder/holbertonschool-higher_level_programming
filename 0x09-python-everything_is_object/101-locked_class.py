#!/usr/bin/python3
""" Write class that prevents user from dynamically creating new instance """


class LockedCLass:
    """ Module: LockedClass is our class """
    __slots__ = "first_name"
