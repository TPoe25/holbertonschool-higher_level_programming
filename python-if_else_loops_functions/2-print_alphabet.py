#!/usr/bin/python3

alphabet = ""

for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'q' and chr(i)!= 'e':
        alphabet += chr(i)
        
print("{}".format(alphabet), end='')