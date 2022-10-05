#!/usr/bin/python3
""" Type validation module """


def size_check(value, name):
    """ Function that checks correct type/value for sizes """
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")

    if value <= 0:
        raise ValueError(f"{name} must be > 0")


def pos_check(value, name):
    """ Function that checks correct type/value for positions """
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")

    if value < 0:
        raise ValueError(f"{name} must be >= 0")
