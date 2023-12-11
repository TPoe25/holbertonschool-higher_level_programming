#!/usr/bin/python3
""" Define a Square class inherited from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Create a Square class """
    def __init__(self, size):
        """ Initialize the Square class """
        super().__init__(size, size)

    def __str__(self):
        """ Return a string representation of the Square class """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
