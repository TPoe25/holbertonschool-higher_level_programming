#!/usr/bin/python3

str = ""

for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) != 'e' and chr(letter) != 'q':
        str += chr(letter)

print(str)
