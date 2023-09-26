#!/usr/bin/python3
""" define a object lookup function"""

def lookup(obj):
    """ return a list of all attributes of an object"""
    return dir(obj)
