#!/usr/bin/python3
""" Task 1 module """


def write_file(filename="", text=""):
    """ write_file function that writes to a file """

    with open(filename, 'w+', encoding="utf-8") as f:

        res = f.write(text)

    return res
