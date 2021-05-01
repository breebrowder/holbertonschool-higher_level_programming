#!/usr/bin/python3
for letters in reversed(range(97, 123)):
    if (letters % 2 == 0):
        print("{}".format(chr(letters)), end="")

    else:
        print("{}".format(chr(letters - 32)), end="")
