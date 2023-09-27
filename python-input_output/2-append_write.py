#!/usr/bin/python3
""" defines a function to read a file """

    
def append_write(filename"", text=""):
    """" Appends text to a file."""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            nb_characters_added = file.write(text)
        return nb_characters_added
    except Exception as e:
        print("An error has occurred:", e)
        return (0)
    
if __name__ == "__main__":
    nb_characters_added = append_write(filename="", text="")