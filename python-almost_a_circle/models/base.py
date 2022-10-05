#!/usr/bin/python3
""" Task 0 module """
import json


class Base():
    """ Base class for future classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        return json.dumps(list_dictionaries)
