#!/usr/bin/python3
""" Task 6 module """


def load_from_json_file(filename):
    """ Function that converts json file to python object """

    import json

    with open(filename, 'r', encoding="utf-8") as f:

        my_str = f.read()

    return json.loads(my_str)
