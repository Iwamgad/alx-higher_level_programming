#!/usr/bin/python3

"""Square module definition.
This module defines a Square class
"""

class Square:
    """A Square class
    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size = 0):
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
    def area(self):
        """Calculates the area of the current square.
        Returns:
            int: The area of the current square.
        """
        return self._Square__size ** 2
    @property
    def size(self):
        """Gets the size of the square.
        Returns:
            int: The size of the current square.
        """
        return self._Square__size
    @size.setter
    def size(self, value):
        """Sets the size of the square.
            int: The size of the current square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size < 0
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value
    def my_print(self):
        """Prints a square with the character #"""
        if self.size:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
