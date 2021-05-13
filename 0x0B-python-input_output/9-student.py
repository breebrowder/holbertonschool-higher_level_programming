#!/usr/bin/python3
""" Write a class Student that defines a student """


class Student():

    def __init__(self, first_name, last_name, age):
        """ Instantiation with public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieving dictionary representation of student """
        return self.__dict__
