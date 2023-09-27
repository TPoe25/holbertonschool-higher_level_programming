#!/usr/bin/python3
""" defines how to write text to a file """

def write_file(filename="", text=""):
    """ writes text to a file """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            nb_characters = file.write(text)
        return (nb_characters)
    except Exception as e:
        print("An error occured:", e)
        return (0)
