#!/usr/bin/python3
""" Module: Write a class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ New class that inherited Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor; defining private instance attr """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returning value of Rect instance """
        squared_x2 = self.__height * self.__width
        return squared_x2

    def display(self):
        """Printing rect to stdout with # """
        for column in range(self.y):
            print("")
        for row in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigning key/value argument to attributes """
        if len(args) != 0:
            ListofA = ["id", "width", "height", "x", "y"]

            for i, arg in enumerate(args):
                setattr(self, ListofA[i], args[i])

        else:
            for key, value in kwargs.items():
                if key is "id" and value is None:
                    setattr(self, "id", self.id)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returning dict repr of rectangle """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y}
