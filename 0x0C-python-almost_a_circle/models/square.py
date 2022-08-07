#!/usr/bin/python3
"""MY square module"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """A square class inherited from rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square object.
        Args:
            size (int): size of the square
            x (int): The x coordinate of the square object
            y (int): The y coordinate of the square object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of a square"""
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Gets size
        Returns:
            int: The width
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets size
        Args:
            value(int): The value to set to width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attributes = ['id', 'size', 'x', 'y']

        for idx, x in enumerate(args):
            if idx >= len(attributes):
                return
            self.__setattr__(attributes[idx], x)

        if args:
            return

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def to_dictionary(self):
        """dict representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x,
                'y': self.y}
