#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxValue = my_list[0]

    for i in range(len(my_list)):
        if maxValue <= my_list[i]:
            maxValue = my_list[i]

    return maxValue
