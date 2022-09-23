#!/usr/bin/python3
""" Task 4 module  """


def print_square(size):
    """ Print square function  """

    if type(size) is int or type(size) is float:
        if size < 0 and type(size) is float:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        for i in range(size):
            print("#" * size)
    else:
        raise TypeError("size must be an integer")
