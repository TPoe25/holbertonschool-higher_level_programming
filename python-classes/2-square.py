#!/usr/bin/python3
""" This is a square class """

class Square:
    """ Square class to store the size of the square."""
    def __init__(self, size=0):
        """ initialize the square """
        """ Args: size (int): size of the square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        self.__size = size