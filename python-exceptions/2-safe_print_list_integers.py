#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    track = 0
    for i in my_list:
        try:
            if isinstance(i, int):
                print("{:d}".format(i), end=" ")
                track += 1
                if track == x:
                    break
        except ValueError:
            pass
        print()
        return track

if __name__ == "__main__":
    
    safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
