#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = a_dictionary.copy()
    for i in tmp:
        if tmp[i] is value:
            del a_dictionary[i]
    return a_dictionary
