#!/usr/bin/python3
""" This defines a rectangle class."""


class Rectangle:
    """ This defines a rectangle class."""
    def __init__(self, width, height):
        """ This defines a rectangle width and height."""
        self.width = width
        self.height = height
        
        @property
        def width(self):
            """ Width of the rectangle """
            return self._width
        
        @width.setter
        def width(self, value):
            """ sets Width of the rectangle """
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self._width = value
            
        @property
        def height(self):
            """ Height of the rectangle """
            return self._height
        
        @height.setter
        def height(self, value):
            """ sets Height of the rectangle """
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if value < 0:
                raise ValueError('height must be >= 0')
            self._height = value