#!/usr/bin/python3
""" defines a function that inherits from another class"""

def inherits_from(obj, a_class):
    """ returns True if obj inherits from a_class """
    return issubclass(obj, a_class)
