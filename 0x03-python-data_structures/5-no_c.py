#!/usr/bin/python3
def no_c(my_string):
    my_new_string = list(my_string)

    for i in my_new_string:
        if i == "c" or i == "C":
            my_new_string.remove(i)
    return "".join(my_new_string)
