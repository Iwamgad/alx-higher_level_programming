#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""My Rectangle class module"""

class Rectangle(BaseGeometry):
    """A rectangle class
    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    """
    def __init__(self, width, height):
        """Initializes a new rectangle object
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
    def area(self):
        """Calculates the area of the rectangle
        """
        return self.width * self.height

    def __str__(self):
        """Returns the print and str reprsentation"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.width) + "/" + str(self.height)
        return string
