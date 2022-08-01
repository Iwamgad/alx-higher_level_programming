#!/usr/bin/python3
"""My list inheritance module"""

class MyList (list):
    """A list class"""

    def print_sorted(self):
        """Prints a list in a sorted manner"""
        print(sorted(self))
