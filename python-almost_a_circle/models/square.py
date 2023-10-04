#!/usr/bin/python3
""" defines the class for square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class that inherits from Rectangle"""
    
    
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor for square

        Args:
            size (int): size of the square
            x (int): uses x coordinate of the square
            y (int): uses y coordinate of the square
            id (_type_): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter for size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """ setter for size"""
        self.width = value
        self.height = value
        
    def __str__(self):
        """ returns a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
