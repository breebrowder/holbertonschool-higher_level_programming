#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for ints in reversed(my_list):
        print("{}".format(ints))
        if (my_list) is None:
            return
