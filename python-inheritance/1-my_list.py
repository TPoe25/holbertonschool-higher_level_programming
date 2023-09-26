#!/usr/bin/python3
""" This function prints the elements of a list in sorted order."""

class MyList(list):
    """ MyList is a subclass of list. """
    def print_sorted(self):
        if issubclass(MyList, list):
            print(sorted(self))