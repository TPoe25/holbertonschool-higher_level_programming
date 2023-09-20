#!/usr/bin/python3
"""" this is square class """

class Square:
    def __init__(self, size=0):
        """ creates a square object """
        self.__size = size
  
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
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
            """ calculates the area of the square """
            """ Return: the area of the square """
            return self.__size ** 2      
if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)