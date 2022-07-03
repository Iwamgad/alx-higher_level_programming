#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_new_list = my_list.copy()

    if idx < 0 and idx > len(my_list):
        return my_list
    else:
        my_new_list[idx] = element
        return my_new_list
