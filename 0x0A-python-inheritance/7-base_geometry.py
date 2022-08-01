#!/usr/bin/python3
"""My Geometry class module"""

class BaseGeometry:
    """A class BaseGeometry (based on 5-base_geometry.py)
    Attributes:
        size (int): The size of the square.
    """
    def area(self):
        """Calculates the area of the geometry
        Raises:
            Exception: If size is not an integer.
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validates a value
        Args:
            name (str): is any string
            value (int): the integer to be validated
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value <= 0
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
