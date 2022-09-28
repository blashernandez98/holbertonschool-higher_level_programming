#!/usr/bin/python3
""" Task 9 module """


class Student():
    """ Student class with basic info """

    def __init__(self, first, last, age):
        """ Initializer  """

        self.first_name = first
        self.last_name = last
        self.age = age

    def to_json(self):
        """ to_json function that returns json of Student """

        return self.__dict__
