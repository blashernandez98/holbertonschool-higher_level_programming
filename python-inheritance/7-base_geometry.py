#!/usr/bin/python3
""" Task 7 module """


class BaseGeometry():
    """ BaseGeometry class """

    def area(self):
        """ area public instance method  """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator function """

        if type(value) is not int:

            raise TypeError(f"{name} must be an integer")

        if value <= 0:

            raise ValueError(f"{name} must be greater than 0")
