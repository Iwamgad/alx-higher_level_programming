#!/usr/bin/python3
def no_c(my_string):
    my_new_string = list(my_string)
    idx = 0
    for index in my_new_string:
        if index == 'c' or index == 'C':
            my_new_string[idx] = ""
        idx += 1
    return "".join(my_new_string)
