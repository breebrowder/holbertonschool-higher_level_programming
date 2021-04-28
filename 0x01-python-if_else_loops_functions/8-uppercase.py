#!/usr/bin/python3
def uppercase(str):
    for chars in str:
        upper = ord(chars)
        if (upper) >= 97 and upper <= 122:
            upper -= 32
            print("{:c}".format(upper), end="")
        else:
            print("")
