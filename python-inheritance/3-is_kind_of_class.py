#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is instance or inherits from class.add

    Args:
        obj (object): Object to check.
        a_class (class): class to check against.
        
    Returns:
    bool: True if object is instance of/inherited class, False otherwise.
    """
    return isinstance(obj, a_class)

if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
        