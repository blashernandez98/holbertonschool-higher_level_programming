#!/usr/bin/python3
""" Task 7 module  """


def int_check(value, var_name):
    """ Type and value check for integers  """

    if type(value) is not int:
        raise TypeError(var_name + " must be an integer")
    if value < 0:
        raise ValueError(var_name + " must be >= 0")


def rectangle_check(obj, var_name):

    if type(obj) != Rectangle:
        raise TypeError(f'{var_name} must be a an instance of Rectangle')


class Rectangle:
    """ Rectangle class  """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
                    string += str(self.print_symbol)
                if i != self.height - 1:
                    string += '\n'

        return string

    def __repr__(self):

        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        rectangle_check(rect_1, "rect_1")
        rectangle_check(rect_2, "rect_2")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
