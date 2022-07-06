#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    TempDict = dict(a_dictionary)
    for key, value in TempDict.items():
        TempDict[key] = value * 2
    return TempDict
