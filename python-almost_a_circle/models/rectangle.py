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
        """ Instantation function """
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
        """ Function that returns area of rectangle """
        return self.width * self.height

    def display(self):
        """ Function that prints rectangle to stdout """
        print('\n'*self.y, end="")
        for i in range(self.height):
            print(' '*self.x, end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Custom str method for Rectangle """
        out = "[Rectangle] "
        out += f"({self.id}) "
        out += f"{self.x}/{self.y} - "
        out += f"{self.width}/{self.height}"

        return out

    def update(self, *args, **kwargs):
        """ Update function updates attributes for Rectangle instance """
        if len(args) == 0:
            attr = ["id", "width", "height", "x", "y"]

            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                pass

    def to_dictionary(self):
        """ Returns dictionary representation of Rectangle instance """
        dic = self.__dict__
        new_dic = {}
        for key, value in dic.items():
            if key == 'id':
                new_dic[key] = value
            else:
                n_key = key[12:]
                new_dic[n_key] = value
        return new_dic
