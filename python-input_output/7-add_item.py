#!/usr/bin/python3
""" defines script that adds all command line arguments to a list"""
import sys
import os.path


if os.path.exists("add_item.json"):
    """ check if the file exists """
    from load_from_json_file import load_from_json_file 
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []
    """ if the file does not exist, create it """

my_list.extend(sys.argv[1:])

from save_to_json_file import save_to_json_file
""" saves the list to a json file """
save_to_json_file(my_list, "add_item.json")
