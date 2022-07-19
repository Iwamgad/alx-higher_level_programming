#!/usr/bin/python3

"""Square module definition.
This module defines a square class
"""

class Square:
    """A simple square  class
    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructs a square object
        Args:
            size (int): The size of the square.
                The default value is 0.
        Raises:
            TypeError: If siz  is not an integer.
            ValueError: If siz  < 0
        """
        self.size = size
        self.position = position

    def __str__(self):
        result = ""
        if self.size:
            line = " " * self.position[0] + "#" * self.size
            result = "\n" * self.position[1]
            result += (line + "\n") * (self.size - 1)
            result += line
        return result

    def area(self):
        """Calculates the area of the current square.
        Returns:
            int: The area of the current square.
        """
        return self.size ** 2

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

    @property
    def position(self):
        """
        Args:
            position (:obj: tuple of int): The position to start to
                print the square .
        Raises:
            TypeError: If position  is not a tuple of 2 integers
        """
        return self._Square__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._Square__position = position

    def my_print(self):
        """Prints a square with the character #"""
        print(self)
