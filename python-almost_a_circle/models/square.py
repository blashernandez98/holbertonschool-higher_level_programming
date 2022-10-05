#!/usr/bin/python3
""" Square class Module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Instantation method """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Custom str method """

        out = "[Square] "
        out += f"({self.id}) "
        out += f"{self.x}/{self.y} - "
        out += f"{self.width}"

        return out

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
