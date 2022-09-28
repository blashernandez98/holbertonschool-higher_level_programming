#!/usr/bin/python3
""" Task 10 module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):

        super().__init__(size, size)
