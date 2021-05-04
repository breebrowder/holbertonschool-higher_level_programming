#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        num = 0
        for num in range(x):
            print("{:d}".format(my_list[num]), end="")

    except IndexError:
        return num

    else:
        return x

    finally:
        print("")
