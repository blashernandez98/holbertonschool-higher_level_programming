#!/usr/bin/python3
""" Task 3 module  """


def int_check(value, var_name):
    """ Type and value check for integers  """

    if type(value) is not int:
        raise TypeError(var_name + " must be an integer")
    if value < 0:
        raise ValueError(var_name + " must be >= 0")


class Rectangle:
    """ Rectangle class  """

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
        self.__height = value

    def __init__(self, width=0, height=0):

        int_check(width, "width")
        int_check(height, "height")

        self.__width = width
        self.__height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):

        if self.width == 0 or self.height == 0:
            return 0

        return (self.width * 2 + self.height * 2)

    def __str__(self):
        string = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                for j in range(self.width):
                    string += '#'
                if i != self.height - 1:
                    string += '\n'

            return string
