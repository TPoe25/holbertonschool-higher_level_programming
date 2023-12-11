#!/usr/bin/python3

def no_c(my_string):
    fresh_string = ""
    for char in my_string:
        if char != "c" and char != "C":
            fresh_string += char
    return fresh_string

if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
