#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    i = 0
    j = 0
    for w_avg in my_list:
        i += (w_avg[0] * w_avg[1])
        j += w_avg[1]
    return (i/j)
