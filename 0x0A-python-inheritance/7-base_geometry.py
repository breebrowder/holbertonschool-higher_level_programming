#!/usr/bin/python3
""" Write a class based on Task 6 """


class BaseGeometry:
    """ Public instance method that raises an exception """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))

        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
