#!/usr/bin/python3

def print_last_digit(num):
    #use modulo operator to get last digit
    last_digit = abs(num) % 10
    print(last_digit, end='')
    return last_digit
