#!/usr/bin/python3
""" define a function to convert a python object to a json string."""
import json


def to_json_string(my_obj):
    """ convert a python object to a json string."""
    return json.dumps(my_obj)
