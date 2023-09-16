#!/usr/bin/python3
def fizzbuzz():
    output = ""
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            output += "FizzBuzz"
        elif num % 3 == 0:
            output += "Fizz"
        elif num % 5 == 0:
            output += "Buzz"
        else:
            output += str(num)
        if num < 100:
            output += " "
    print(output.strip(), end="")
