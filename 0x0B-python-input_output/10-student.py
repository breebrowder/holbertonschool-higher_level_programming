#!/usr/bin/python3
""" Write a class Student that defines a student """


class Student():

    def __init__(self, first_name, last_name, age):
        """ Instantiation with public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieving dictionary representation of student """
        if attrs is None:
            return self.__dict__
            """ attrs is a list of strings; want attribute names retrieved """
        else:
            All = {}
            for atrname in attrs:
                if atrname in self.__dict__:
                    All[atrname] = self.__dict__[atrname]
            return All
