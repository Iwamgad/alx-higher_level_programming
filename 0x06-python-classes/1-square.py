#!/usr/bin/python3

"""Square module definition.
This module defines a`Square` class
"""

class Square:
    """A ``Square`` class
    Attributes:
        size (int): The size of the ``Square``.
    """
    def __init__(self, size):
        """Initializes a new ``square`` object.
        Args:
            size (int): The size of the square.
        """
        self._size = size
