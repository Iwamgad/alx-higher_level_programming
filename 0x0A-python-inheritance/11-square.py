#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""My Square class module"""

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
        self.size = size
    def area(self):
        """Calculates the area of the square
        """
        return self.size ** 2

    def __str__(self):
        """Returns the print and str reprsentation"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.size) + "/" + str(self.size)
        return string
