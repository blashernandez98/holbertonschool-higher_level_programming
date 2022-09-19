#!/usr/bin/python3
""" Task 1 module """
""" Error check function for positive integers """


def int_check(value):
    if (type(value) != int):
        raise TypeError("size must be an integer")
        return False
    if (value < 0):
        raise ValueError("size must be >= 0")
        return False
    return True


""" Square class representing a square """


class Square():
    """ Square class """
    def __init__(self, size=0):
        if (int_check(size)):
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if (int_check(size)):
            self.__size = size

    def area(self):
        return self.__size ** 2
