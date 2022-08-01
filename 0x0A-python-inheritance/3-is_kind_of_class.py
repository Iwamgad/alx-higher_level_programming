#!/usr/bin/python3
"""My instance check module"""

def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of, or if the object is an instance
       of a class that inherited from, the specified class
    Args:
         obj(any) = the object to check
         a_class(type) = the class to check the instance from
    Return:
           True if the object is exactly an instance
           otherwise False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
