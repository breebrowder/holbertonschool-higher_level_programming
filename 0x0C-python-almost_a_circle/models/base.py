#!/usr/bin/python3
""" Class Base used to manage id attribute in all future classes """

import json
from os import path


class Base:
    """ Private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiation """
        if id is not None:
            self.id = id
        else:
            """ Increment objects & assign new value to public inst attr id """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Update class to add static method that returns JSON string repr """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        reprList = []
        if list_objs is not None:
            for i in list_objs:
                reprList.append(cls.to_dictionary(i))
        with open(filename, mode="w", encoding="utf-8") as myFile:
            myFile.write(cls.to_json_string(reprList))

    @staticmethod
    def from_json_string(json_string):
        """ Returning list of the JSON string repr """
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)
