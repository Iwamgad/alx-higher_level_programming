#!/usr/bin/python3

"""
This module defines a rectangle class
"""
class Rectangle:
    """A rectangle class
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle object.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.  
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Getter - gets value of width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter- sets the value of width
            Args:
                value(int): the value to set to width
            """

            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise TypeError("width must be >= 0")

            self.__width = value

        @property
        def height(self):
            """Getter - gets value of height"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter- sets the value of height
            Args:
                value(int): the value to set to height
            """

            if type(value) != int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise TypeError("height must be >= 0")

            self.__height = value
