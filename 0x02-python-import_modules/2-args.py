#!/usr/bin/python3
import sys

argNums = len(sys.argv) - 1

if (argNums == 0):
    print("{:d} arguments.".format(argNums))
elif (argNums == 1):
    print("{:d} argument:".format(argNums))
    print("{:d}: {:d}".format(argNums, sys.argv[argNums]))
else:
    print("{:d} arguments:".format(argNums))
    for i in range(1, argNums + 1):
        print("{:d}: {:}".format(i, sys.argv[i]))
