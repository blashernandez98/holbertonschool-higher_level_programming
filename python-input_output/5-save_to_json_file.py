#!/usr/bin/python3
""" Task 5 module """


def save_to_json_file(my_obj, filename):
    """ Function that writes JSON representation of object to file """

    import json

    with open(filename, 'w+', encoding="utf-8") as f:

        f.write(json.dumps(my_obj))
