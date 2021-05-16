#!/usr/bin/python3
import sys
j = 0
trueLength = len(sys.argv)
if __name__ == "__main__":
    for index in range(1, trueLength):
        j += int(sys.argv[index])
    print("{:d}".format(j))
