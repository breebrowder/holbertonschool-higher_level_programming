#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """ add public instance method that prints the list, but sorted """
    def print_sorted(self):

        print(sorted(self))
