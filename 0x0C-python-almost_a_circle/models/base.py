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
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returning instance with attr set; using update to create dummy """
        if cls.__name__ == "Rectangle":
            dummyList = cls(6, 6)
        if cls.__name__ == "Square":
            dummyList = cls(6)
        dummyList.update(**dictionary)
        return dummyList

    @classmethod
    def load_from_file(cls):
        """ Updating class by returning list of special instances """
        filename = cls.__name__ + ".json"
        instances = []

        if path.exists(filename) is False:
            return []
        if path.exists(filename):
            with open(filename, mode="r", encoding="utf-8") as myFile:
                f = myFile.read()
                List = cls.from_json_string(f)
            for dict in List:
                instances.append(cls.create(**dict))
            return instances
