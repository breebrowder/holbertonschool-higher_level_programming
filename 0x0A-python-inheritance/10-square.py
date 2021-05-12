#!/usr/bin/python3
""" write a class that inherits another class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiation with constructor """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.__width = size
        self.__height = size

    def area(self):
        return self.__width * self.__height
