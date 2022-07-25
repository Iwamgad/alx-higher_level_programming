#!/usr/bin/python3
"""
    My square printer module
"""

def print_square(size):
    """Prints a square with the character #
    Args:
        size(int): The size of the square
    Raises:
        TypeError:  If size is not an integer
                    If size is a float and is less than 0
        ValueError: If size is less than 0
    """
    # Checks for errors
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    # Prints a square with the character #
    if size:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
    else:
        print()
