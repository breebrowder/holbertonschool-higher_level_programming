#!/usr/bin/python3
""" Writing the class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Base for Rectangle: Class constructor below """

def __init__(self, width, height, x=0, y=0, id=None):
    """ Private instance attributes, each with own public getter and setter """
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    super().__init__(id)
