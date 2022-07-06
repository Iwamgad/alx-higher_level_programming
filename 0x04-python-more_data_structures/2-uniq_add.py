#!/usr/bin/python3
def uniq_add(my_list=[]):
    MyNewList = []
    Sum = 0
    for x in my_list:
        if x not in MyNewList:
            MyNewList.append(x)
    for y in MyNewList:
        Sum += y
    return Sum
