#!/usr/bin/python3
""" define a base class for geometry """


class BaseGeometry:
    """ define a base class for geometry """
    def area(self):
        """ Raise an exception if not implemented """
        raise Exception("area() not implemented")
