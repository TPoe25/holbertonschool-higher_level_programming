#!/usr/bin/python3

for first in range(10):
    for second in range(10):
        print("{:d}{:d}".format(first, second), end=", " if second < 9 else "\n")
        