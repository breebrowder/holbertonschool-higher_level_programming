#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv)

    if (args > 2):
        print("{} arguments:".format(args - 1))

    elif (args == 2):
        print("{} argument:".format(args - 1))

    else:
        print("{} arguments.".format(args - 1))

    for position, arg in enumerate(argv[1:0]):
        print("{}: {}".format(position + 1, arg))
