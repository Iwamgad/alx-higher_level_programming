#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 0:
        return tuple_b
    elif len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_a) == len(tuple_b):
        temp_tuple = tuple_a
        new_tuple = list(temp_tuple)
        i = 0
        while i < len(tuple_a):
            new_tuple[i] = tuple_a[i] + tuple_b[i]
            i = i + 1
        new_tuple = tuple(new_tuple)
    else:
        if len(tuple_a) < len(tuple_b):
            maxIndex = len(tuple_a)
            temp_tuple = tuple_b
            new_tuple = list(temp_tuple)
        else:
            temp_tuple = tuple_a
            new_tuple = list(temp_tuple)
            maxIndex = len(tuple_b)
        i = 0
        while i < maxIndex:
            new_tuple[i] = tuple_a[i] + tuple_b[i]
            i = i + 1
        new_tuple = tuple(new_tuple)
    return new_tuple
