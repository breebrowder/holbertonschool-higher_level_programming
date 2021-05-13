#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv)
    result = 0

    if (args > 2):
        for i in range(1, args):
            argv[i] = int(argv[i])
            result += argv[i]
            print(result)
    elif (args == 1):
        print(0)
    else:
        print(argv[1])
