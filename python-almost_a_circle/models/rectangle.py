#!/usr/bin/python3
"""defines the rectangle class """


from models.base import Base


class Rectangle(Base):
    """acts as a rectangle inherited from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor for Rectangle
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
                x (int): x position of the rectangle
                y (int): y position of the rectangle
                id (int): id of the rectangle
        """
        super().__init__(id)  # calling superclass constructor with id

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x position of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y position of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ calculates the display of the rectangle"""
        for _ in range(self.__height):
            print("#" * self.__width)
