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
        """ Converts list of dictionaries to json string """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_obj):
        """ Saves list of objects to file as json string """
        if "Square" in f"{cls}":
            cls_name = "Square"
        if "Rectangle" in f"{cls}":
            cls_name = "Rectangle"
        if list_obj is None:
            string = "[]"
        else:
            dictionaries = list(map(lambda x: x.to_dictionary(), list_obj))
            string = Base.to_json_string(dictionaries)

        with open(f"{cls_name}.json", 'w', encoding="utf-8") as f:
            f.write(string)
