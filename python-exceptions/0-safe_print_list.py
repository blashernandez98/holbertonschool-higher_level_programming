#!/usr/bin/python3


def safe_print_list(my_list, x):

    i = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return i

    except IndexError:
        print()
        return i
