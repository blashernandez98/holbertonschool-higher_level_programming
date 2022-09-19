#!/usr/bin/python3
""" Task 1 module """


class Square():
    """ Square class """
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    """ Area method that returns area of the square """
    def area(self):
        return self.__size**2
