#!/usr/bin/python3
""" defines how to import student module"""

class Student:
    """ student class module"""
    def __init__(self, first_name, last_name, age):
        """construct for students

        Args:
            first_name (int): first name of student
            last_name (int): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """construct for student attributes to json

        Args:
            attrs (int): attributes of student
        """
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
