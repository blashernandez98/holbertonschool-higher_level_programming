#!/usr/bin/python3
""" Task 6  module """
""" Error check function for positive integers """


def int_check(value):
    if (type(value) != int):
        raise TypeError("size must be an integer")
        return False
    if (value < 0):
        raise ValueError("size must be >= 0")
        return False
    return True


""" Error check function for tuple of 2 positive integers  """


def int_tuple_check(tup):
    res = True
    if (type(tup) != tuple):
        res = False
    for i in range(0, 2):
        if (type(tup[i]) != int or tup[i] < 0):
            res = False
    if (res is False):
        raise TypeError("position must be a tuple of 2 positive integers")
    return res


""" Square class representing a square """


class Square():
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        if (int_check(size)):
            self.__size = size
        if (int_tuple_check(position)):
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if (int_check(size)):
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (int_tuple_check(position)):
            self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        size = self.size
        if not size:
            print()
            return
        for i in range(size):
            print(" "*self.__position[0], end="")
            for i in range(size):
                print("#", end="")
            print()
