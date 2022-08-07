#!/usr/bin/python3
"""MY rectangle module"""
from models.base import Base

class Rectangle(Base):
    """A rectangle class inherited from base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle object.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle object
            y (int): The y coordinate of the rectangle object
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets width
        Returns:
            int: The width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Sets width
        Args:
            value(int): The value to set to width
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        self.raiseError(width, 'width')
        self.__width = width

    @property
    def height(self):
        """Gets height
        Returns:
            int: The height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height
        Args:
            value(int): The value to set to width
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        self.raiseError(height, 'height')
        self.__height = height

    @property
    def x(self):
        """Gets x
        Returns:
            int: The x value
        """
        return self.__x
    @x.setter
    def x(self, x):
        """Sets x
        Args:
            value(int): The value to set to x
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        self.raiseError(x, 'x')
        self.__x = x

    @property
    def y(self):
        """Gets y
        Returns:
            int: The y value
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Sets y
        Args:
            value(int): The value to set to y
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        self.raiseError(y, 'y')
        self.__y = y

    def raiseError(self, attribute, name):
        """Raises errors"""
        if type(attribute) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name in ['width', 'height']:
            if attribute <= 0:
                raise ValueError("{} must be > 0".format(name))
        if name in ['x', 'y']:
            if attribute < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Returns Area of rectangle"""
        return self.width * self.height

    def display(self):
        """Displays # in a rectangle form"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print("", end="") for x in range(self.x)]
            [print('#', end="")for j in range(self.width)]
            print()

    def __str__(self):
        """Overrides str method from Base"""
        ret = f"[Rectangle] ({self.id}) {self.x}/{self.y} "
        ret += f"- {self.width}/{self.height}"
        return ret

    @staticmethod
    def generate_setter(name, value):
        """Return the setter in literal for do an evaluation"""
        setter = 'self.{} = {}'.format(name, value)
        return setter

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attributes = ['id', 'width', 'height', 'x', 'y']

        for index, x in enumerate(args):
            if index >= len(attributes):
                return

            self.__setattr__(attributes[index], x)

        if args:
            return

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def to_dictionary(self):
        """Return the dictionary representation of a rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
