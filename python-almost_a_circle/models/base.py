#!/usr/bin/python3
""" this is a definition of base class """


import json


class Base:
    """ represents a base class for all"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ base class constructor
            Args:
                id (int): The id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)


    @classmethod
    def validate_id(cls, id):
        """ validates the id attribute of a dictionary"""
        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
            elif id <= 0:
                raise ValueError("id must be > 0")
