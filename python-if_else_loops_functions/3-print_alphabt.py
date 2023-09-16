#!/usr/bin/python3
output = ""

for char in "abcdefghijklmnopqrstuvwxyz":
    if char != 'e' and char != 'q':
        output += char

print("{}".format(output), end='')
