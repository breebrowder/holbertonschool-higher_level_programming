#!/usr/bin/python3
for leftnum in range(0, 10):
    for rightnum in range(leftnum + 1, 10):
        if leftnum == 8 and rightnum == 9:
            print("{:d}{:d}".format(leftnum, rightnum))
        else:
            print("{:d}{:d}".format(leftnum, rightnum), end= ", ")
