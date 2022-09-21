#!/usr/bin/python3
""" TASK 0 module  """


def add_integer(a, b=98):
    """ Adition function  """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)
    return a + b
