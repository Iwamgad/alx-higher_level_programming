#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argNums = len(sys.argv) - 1

    if (argNums == 0):
        print("{} arguments.".format(argNums))
    elif (argNums == 1):
        print("{} argument:".format(argNums))
        print("{}: {}".format(argNums, sys.argv[argNums]))
    else:
        print("{} arguments:".format(argNums))
        for i in range(1, argNums + 1):
            print("{}: {}".format(i, sys.argv[i]))
