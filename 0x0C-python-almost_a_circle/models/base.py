#!/usr/bin/python3
""" Write the first class Base """


class Base:

    __nb_objects = 0
    """ Private class attribute """

    def __init__(self, id=None):
        """ Instantiation """
        if id is not None:
            self.id = id
        else:
            """ Increment objects & assign new value to public inst attr id """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
