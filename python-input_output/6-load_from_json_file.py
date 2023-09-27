#!/usr/bin/python3
""" define function to save object to json file """
import json


def load_from_json_file(filename):
    """ create function to load from json file """
    with open(filename, 'r') as file:
        return json.load(file)
