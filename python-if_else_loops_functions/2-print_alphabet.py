#!/usr/bin/python3

result = ""

for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) != 'e' and chr(letter) != 'q':
        result += chr(letter)

print(result)
