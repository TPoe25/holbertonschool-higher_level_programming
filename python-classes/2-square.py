#!/usr/bin/python3

class Square:
    """
    Square class
    """
    def __init__(self, size=0):
        """
        initialize the square
        
        Args:
            size (int): size of the square
        
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be a positive integer")
        self.__size = size
# isinstance(size, int) to check if the size is an integer
#__self to access the square object private attribute