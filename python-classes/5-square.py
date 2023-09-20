#!/usr/bin/python3
""" define a square class """

class Square:
    """ this is a square class """
    
    def __init__(self, size=0):
        """ initialize the square """
        """ Args: size (int): the size of the square """
        self.size = size
    
    @property
    def size(self):
        """ get the size of the square """
        """ Returns: size (int): the size of the square """
        return self._size
    
    @size.setter
    def size(self, value):
        """ set the size of the square """
        """ Args: value (int): the size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
        
    def area(self):
        """ get the area of the square """
        """ Returns: area (int): the area of the square """
        return self.size ** 2
    
    def my_print(self):
        """ print the square """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)