#!/usr/bin/python3

"""Square module definition.
This module defines a`Square` class
"""

class Square:
    """defines a square by: (based on 1-square.py)"""
    def __init__(self, size):
        """Initializes a new ``square`` object.
        Args:
            size (int): The size of the square.
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
