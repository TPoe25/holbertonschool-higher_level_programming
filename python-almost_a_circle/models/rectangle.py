#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """ rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initalizes a rectangle"""
        
        super().__init__(id) # calling superclass constructor with id
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
    @property
    def width(self):
        """getter for the width of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for the width of the rectangle"""
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height of the rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """ setter for the height of the rectangle"""
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for the x position of the rectangle"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """ setter for the x position of the rectangle"""
        if not isinstance(value, int):
            raise ValueError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for the y position of the rectangle"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """getter for the y position of the rectangle"""
        if not isinstance(value, int):
            raise ValueError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
