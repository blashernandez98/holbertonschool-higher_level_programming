#!/usr/bin/python3
""" Task 10 module """


class Student():
    """ Student class with basic info """

    def __init__(self, first, last, age):
        """ Initializer  """

        self.first_name = first
        self.last_name = last
        self.age = age

    def to_json(self, attrs=None):
        """ to_json function that returns json of Student """

        dic = self.__dict__

        if attrs is None:

            return dic

        new_dic = {key: dic[key] for key in attrs if key in dic}

        return new_dic

    def reload_from_json(self, json):

        for key in json.keys():

            self.key = json[key]
