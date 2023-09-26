#!/usr/bin/python3
""" This function prints the elements of a list in sorted order."""
class MyList(list):
    """ MyList is a subclass of list. """
    def print_sorted(self):
        """ print_sorted() prints the elements of list in sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
