#!/usr/bin/python3
"""
    My name concatenator module
"""

def say_my_name(first_name, last_name=""):
    """Prints a concatenated name (<first name> <last name>)
    Args:
        first_name(str): The first name
        last_name(str): The last name
    Raises:
        TypeError:  If first_name and last_name are not strings
    """
    # Checks if the first_name and last_name are stringss
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
