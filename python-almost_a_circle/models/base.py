#!/usr/bin/python3

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
            if id <= 0:
                raise ValueError("id must be > 0")
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
