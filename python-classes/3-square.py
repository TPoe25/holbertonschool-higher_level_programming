#!/usr/bin/python3

class Square:
    """
    Square class
    """
    def __init__(self, size):
        """
        Initalize the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """
        Gets the area of the square
        """
        return self.__size ** 2
    