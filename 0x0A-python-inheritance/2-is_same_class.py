#!/usr/bin/python3
"""My instance check module"""

def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class
    Args:
         obj(any) = the object to check
         a_class(type) = the class to check the instance from
    Return:
           True if the object is exactly an instance
           otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
