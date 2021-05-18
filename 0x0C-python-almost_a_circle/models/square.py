#!/usr/bin/python3
""" Module: Class Square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inherited from Class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """ Assigning key/value argument to attribites """
        if len(args) != 0:
            ListofA = ["id", "size", "x", "y"]

            for i, arg in enumerate(args):
                setattr(self, ListofA[i], args[i])

        else:
            for key, value in kwargs.items():
                if key is "id" and value is None:
                    setattr(self, "id", self.id)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returning dict repr of square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y}
