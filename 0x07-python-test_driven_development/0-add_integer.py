#!/usr/bin/python3
"""
    My addition module
"""

def add_integer(a, b=98):
    """Adds two integers
    Args:
        a (int or float): First parameter
        b (int or float): Second Parameter
    Returns:
        int: The sum of the two numbers
    Raises:
        TypeError: If a or b are not integers or floats
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if not type(a) is int:
        raise TypeError("a must be an integer")
    elif not type(b) is int:
        raise TypeError("b must be an integer")
    else:
        return a + b
