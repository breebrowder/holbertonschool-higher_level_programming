#!/usr/bin/python3
""" Writing a class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):

    """ Class constructor below """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Private instance attr; each with own getter and setter """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if (width <= 0):
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if (height <= 0):
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if (x < 0):
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if (y < 0):
            raise ValueError("y must be >= 0")
