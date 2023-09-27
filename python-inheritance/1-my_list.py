#!/usr/bin/python3
"""
This function prints the elements of a list in sorted order
"""


class MyList(list):
    """
    MyList is a subclass of list with custom print_sorted method
    """
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order
        """
        if issubclass(MyList, list):
            print(sorted(self))
