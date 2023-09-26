#!/usr/bin/python3

def is_same_class(obj, a_class):
    """check if object is a class of a_class

    Args:
        obj (object): class to check
        a_class (class): class to compare
    
    Returns:
    bool: True if object is a class of a_class, False otherwise
    """
    return type(obj) is a_class

if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
