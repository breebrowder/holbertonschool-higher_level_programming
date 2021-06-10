#!/usr/bin/python3

"""  A square that defines a square by: private instance attribute: size,
instantation with optional size, raising TypeError or ValueError, and
public instance method that returns square area """


class Square:

    """ a class that initializes a function within a class: self is the
      reference to the new object being created """

    def __init__(self, size=0):
        """ Init of private size variable """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        squared_x2 = self.__size * self.__size
        return squared_x2

    def my_print(self):
        if self.__size is 0:
            print("")
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print("")
