#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    
    maxVal = my_list[0]
    for number in my_list:
        if number > maxVal:
            maxVal = number
            
    return maxVal

if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
