#!/usr/bin/python3
"""
My locked class module
"""

class LockedClass:
    """object prevents dynamic attribute"""

    __slots__ = ['first_name']
