#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_ints = set()
    
    result = 0
    
    for number in my_list:
        if number not in unique_ints:
            unique_ints.add(number)
            result += number
            
    return result

if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
