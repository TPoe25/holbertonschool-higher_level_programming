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

    def to_dictionary(self):
        """ returns a dictionary representation of the square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }
    
    def update(self, *args, **kwargs):
        """ assigns attributes to square with *args and **kwargs"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
