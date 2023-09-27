#!/usr/bin/python3
""" defines a square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ creating a square class """
    def __init__(self, size):
        """ initializes the square class """
        super().__init__(size, size)
        
    def __str__(self):
        """ returns a string representation of the square class """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)