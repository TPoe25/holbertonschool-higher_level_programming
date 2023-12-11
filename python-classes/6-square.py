#!/usr/bin/python3
""" defines square class"""
class Square:
    """ defines square class"""
    def __init__(self, size = 0, position=(0, 0)):
      """ initalizes square class """
      """ Args: size (int): size of the square """
      """       position (tuple): position of the square """
      self.size = size
      self.__position = position
    
    @property
    def size(self):
       """ getter for size """
       """Returns: size (int): size of the square """
       return self.__size

    @size.setter
    def size(self, value):
        """ setter for size """
        """Args: size (int): size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self, value):
        """ setter for position """
        """Args: value (tuple): position of the square """
        if not isinstance(value, tuple) or len(value)!= 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value
        
    def area(self):
        """ calculates area of the square """
        """ Returns: area (float): area of the square """
        return self.__size ** 2
    
    def my_print(self):
        """ prints the square """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " *self.__position[0], end="")
                print("#" * self.__size)