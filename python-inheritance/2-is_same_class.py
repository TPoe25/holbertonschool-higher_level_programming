#!/usr/bin/python3
"""
defines a class to check if an object is a class of a_class
"""

def is_same_class(obj, a_class):
    """check if object is a class of a_class

    Args:
        obj (object): class to check
        a_class (class): class to compare
    
    Returns:
    bool: True if object is a class of a_class, False otherwise
    """
    return (type(obj) is a_class)