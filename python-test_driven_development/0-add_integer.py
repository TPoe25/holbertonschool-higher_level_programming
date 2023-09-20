#!/usr/bin/python3

def add_integer(a, b = 98):
    """
    Adds two integers together and returns the sum.

    Args: 
        a (int or float): first int or float
        b (int or float, optional): second int or float. Default to 98.

    Returns:
        int: sum of a and b as integer.

    Example:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)