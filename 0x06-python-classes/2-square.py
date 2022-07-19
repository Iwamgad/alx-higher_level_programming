#!/usr/bin/python3

"""Square module definition.
This module defines a Square class
"""

class Square:

    """A Square class
    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """Initializes a new square object.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size < 0
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
