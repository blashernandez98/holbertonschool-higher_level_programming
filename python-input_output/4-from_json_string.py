#!/usr/bin/python3
""" Task 4 module """


def from_json_string(my_str):
    """ Function that converts json to python object """

    import json

    return json.load(my_str)
