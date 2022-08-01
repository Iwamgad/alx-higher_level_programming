#!/usr/bin/python3
"""My Square class module"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A square class
    Attributes:
        size (int): the width of the square
    """
    def __init__(self, size):
        """Initializes a new square object
        Args:
            size (int): the width of the square
        """
        self.integer_validator("size", size)
        self.__size = size
    def area(self):
        """Calculates the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """Returns the print and str reprsentation"""

        string = "[" + str(super().__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
