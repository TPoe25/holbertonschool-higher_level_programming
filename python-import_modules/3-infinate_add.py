#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    x = 0
    for argument in sys.argv:
        if x != 0:
            total += int(argument)
            x += 1
        print(total)
