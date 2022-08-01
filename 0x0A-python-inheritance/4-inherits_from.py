#!/usr/bin/python3
"""My instance check module"""

def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class
       that inherited (directly or indirectly) from the specified class
    Args:
         obj(any) = the object to check
         a_class(type) = the class to check the instance from
    Return:
           True if the object is exactly an instance
           otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
