#!/usr/bin/python3


def safe_print_list(my_list, x):

    printed = 0

    for i in range(x):        
        try:   
            print(my_list[i], end="")
            printed += 1

        except IndexError:
            break

    print()
    return printed
