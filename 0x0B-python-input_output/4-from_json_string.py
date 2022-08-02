#!/usr/bin/python3
"""My object representation module"""
import json

def from_json_string(my_str):
    """Returns the JSON string
    representation of an object
    """
    return json.loads(my_str)
