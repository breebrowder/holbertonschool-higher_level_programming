#!/usr/bin/python3
""" write a class based on previous task """


class BaseGeometry:
    """ raise an exception with a message """
    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))

        elif (value <= 0):
            raise ValueError("{} must be  greater than 0".format(name))
