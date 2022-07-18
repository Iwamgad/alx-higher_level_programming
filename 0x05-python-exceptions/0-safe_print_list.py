#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print(my_list[i], end="")
    except IndexError:
        numElements = 0
        for i in my_list:
            numElements += 1
        return numElements
    else:
        return x
    finally:
        print(end="\n")
