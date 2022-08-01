#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""My Rectangle class module"""

class Rectangle(BaseGeometry):
    """A rectangle class
    """
    def __init__(self, width, height):
        """Initializes a new rectangle object
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        Raises:
            AttributeError: if attribute is null
        """
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
