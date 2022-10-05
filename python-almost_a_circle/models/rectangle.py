#!/usr/bin/python3
""" Task 2 module """
from models.base import Base
from models.type_check import *


class Rectangle(Base):
    """ Rectangle class """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        size_check(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        size_check(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        pos_check(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        pos_check(value, "y")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        size_check(width, "width")
        size_check(height, "height")
        self.__width = width
        self.__height = height
        pos_check(x, "x")
        pos_check(y, "y")
        self.__x = x
        self.__y = y

    def area(self):

        return self.width * self.height

    def display(self):

        print('\n'*self.y, end="")
        for i in range(self.height):
            print(' '*self.x, end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):

        out = "[Rectangle] "
        out += f"({self.id}) "
        out += f"{self.x}/{self.y} - "
        out += f"{self.width}/{self.height}"

        return out

    def update(self, *args):

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except Exception:
            pass