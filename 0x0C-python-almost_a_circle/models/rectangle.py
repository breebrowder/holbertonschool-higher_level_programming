#!/usr/bin/python3
"""This module is for Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):

    """This is the base for the rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """This is to find the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ("")
        rect = ""
        for yspaces in range(self.y):
            print()
        for i in range(self.height):
            for xspaces in range(self.x):
                rect += " "
            for j in range(self.width):
                rect += "#"
            if i != self.height - 1:
                rect += ("\n")
        print(rect)

    def update(self, *args):
        """Replacing items with updated args"""
        if len(args):
            for i, e in enumerate(args):
                if i == 0:
                    self.id = e
                if i == 1:
                    self.width = e
                if i == 2:
                    self.height = e
                if i == 3:
                    self.x = e
                if i == 4:
                    self.y = e

    def __str__(self):
        """Returning in format [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
