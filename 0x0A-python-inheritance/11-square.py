#!/usr/bin/python3
""" Write a class that inherits another class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiation with constructor """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
