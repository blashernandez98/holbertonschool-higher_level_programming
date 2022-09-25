#!/usr/bin/python3
""" Task 1 module  """


class Rectangle:
    """ Rectangle class  """

    @staticmethod
    def int_check(value, var_name):

        if type(value) is not int:
            raise TypeError(var_name + " must be an integer")
        if value < 0:
            raise ValueError(var_name + " must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        int_check(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        int_check(value, "height")
        self.__width = value

    def __init__(self, width=0, height=0):

        int_check(width, "width")
        int_check(height, "height")

        self.__width = width
        self.__height = height
