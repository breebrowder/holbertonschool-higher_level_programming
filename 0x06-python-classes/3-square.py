#!/usr/bin/python3

""" A square that defines a square by: private instance attribute: size,
instantation with optional size, raising TypeError or ValueError, and
public instance method that returns square area """


class Square:

    """ a class that initializes a function within a class: self is the
      reference to the new object being created """

    def __init__(self, size=0):
        """ Init of private size attribute """
        self.__size = size

        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        squared_x2 = self.__size * self.__size
        return squared_x2
