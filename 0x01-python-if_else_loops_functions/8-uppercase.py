#!/usr/bin/python3
def uppercase(str):
    for characters in str:
        upper = ord(characters)
        if (upper) >= 65 and upper <= 90:
            print("{:c}".format(upper), end= " ")
