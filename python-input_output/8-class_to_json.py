#!/usr/bin/python3
""" defines class to json method"""

def class_to_json(obj):
    """serializes an object into a dictionary

    Args:
        obj: The object to serialize
        
    Returns:
        A dictionary representation of the object
    """

    obj_attributes = obj.__dict__

    serializable_attributes = {}

    for key, value in obj_attributes.items():
    
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value
        
    return serializable_attributes
