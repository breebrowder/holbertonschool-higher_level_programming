#!/usr/bin/python3
""" Class Base used to manage id attribute in all future classes """


class Base:
    """ Private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiation """
        if id is not None:
            self.id = id
        else:
            """ Increment objects & assign new value to public inst attr id """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
