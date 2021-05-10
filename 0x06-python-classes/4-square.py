#!/usr/bin/python3

""" A square that defines a square by: private instance attribute: size,
instantation with optional size, raising TypeError or ValueError, and
public instance method that returns square area """


class Square:

    """ a class that initializes a function within a class: self is the
      reference to the new object being created """

    def __init__(self, size=0):
        """ Init of private size variable"""

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        squared_x2 = self.__size * self.__size
        return squared_x2
