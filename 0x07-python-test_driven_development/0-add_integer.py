#!/usr/bin/python3
"""
Function that adds two integers.
"""

def add_interger(a, b=98):
    """
    Function that checks for typr error and
    return the addition of two cast intergers.
    """
    if isinstance(a, bool):
        raise TypeError("a must be an interger")
    if isinstance(b, bool):
        raise TypeError("b must be an interger")
    if not isinstance(a, (float, int)):
        raise TypeError("a must bebe an interger")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an interger")

    return int(a) + int(b)
