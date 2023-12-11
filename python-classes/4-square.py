#!/usr/bin/python3
"""" this is square class """

class Square:
    """ square class """
    def __init__(self, size=0):
        """ creates a square object """
        """ Args: size: the size of the square """
        self.size = size
  
    @property
    def size(self):
        """ gets the size of the square """
        """ Return: the size of the square """
        return self.__size
        
    @size.setter
    def size(self, value):
        """ sets the size of the square """
        """ Args: value: the size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """ calculates the area of the square """
        """ Return: the area of the square """
        return self.__size ** 2