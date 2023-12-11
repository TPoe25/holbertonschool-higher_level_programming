#!/usr/bin/python3
""" define a function to convert a JSON string to data structure """
import json


def from_json_string(my_str):
    """ convert a JSON string """
    return json.loads(my_str)
