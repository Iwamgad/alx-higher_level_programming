#!/usr/bin/python3
"""My Rectangle class module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A rectangle class
    """
    def __init__(self, width, height):
        """Initializes a new rectangle object
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the print and str reprsentation"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
