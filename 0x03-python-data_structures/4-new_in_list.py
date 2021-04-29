#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    cpylist = my_list[:]
    if idx >= 0 < len(cpylist):
        cpylist[idx] = element
    return cpylist
