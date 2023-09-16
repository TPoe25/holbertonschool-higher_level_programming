#!/usr/bin/python3
#for looping through the alphabet and ord ascii characters
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print("{}".format(chr(i)), end='')
        
print()