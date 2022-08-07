#!/usr/bin/python3
"""MY base module"""
import json

class Base:
    """A Base class
    Attributes:
        __nb_object (int): Private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base object.
        Args:
            id (int): Instance attribute for unique number
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jasonfile:
            if list_objs is None:
                jasonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jasonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
           dictionary (**)= a double pointer to a dictionary
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filname = cls.__name__ + '.json'
        new = []

        try:
            with open(filname) as f:
                content = f.read()

        except:
            return new

        json_file = Base.from_json_string(content)
        for obj in json_file:
            new.append(cls.create(**obj))
        return new
