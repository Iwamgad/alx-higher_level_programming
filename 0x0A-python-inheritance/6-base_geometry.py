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
