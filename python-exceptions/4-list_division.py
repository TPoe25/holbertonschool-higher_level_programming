#!/usr/bin/python3

def list_division(my_list1, my_list2, list_length):
    answer = []
    for i in range(list_length):
        try:
            divide = 0
            if isinstance(my_list1[i], (int, float)) and isinstance(my_list2[i], (int, float)):
                if my_list2[i] == 0:
                    raise ZeroDivisionError("division by 0")
                divide = my_list1[i] / my_list2[i]
            else:
                raise TypeError("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            answer.append(divide)
    return answer

if __name__ == "__main__":
    
    list_division = __import__('4-list_division').list_division

    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
