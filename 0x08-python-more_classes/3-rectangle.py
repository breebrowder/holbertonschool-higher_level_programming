#!/usr/bin/python3
""" Creating a new class """


class Rectangle:
    """ Defining rectangle: will have its own set of attributes and methods.
    Using decorators to turn attributes into seperate funcs that will be called
    in wrapper """

    def __init__(self, width=0, height=0):
        """ Initializing method within a class that will recieve the
        instance as the first arg: self; self handles all instances """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieving private instance attribute: width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setting private instance attribute: width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieving private instance attribute: height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setting private instance attribute: height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        squared_x2 = self.__height * self.__width
        return(squared_x2)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0

        perimeter = 2 * (self.__height + self.__width)
        return perimeter

        """ Sometimes you have to google how to find the perimeter of
        a rectangle and it is that simple: p = 2(l + w) """

    def __str__(self):
        tmp = ""
        if self.width is 0 or self.height is 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                tmp += "#"
            else:
                if i == self.height - 1:
                break
                tmp += "\n"
        return tmp
