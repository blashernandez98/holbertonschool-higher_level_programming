#!/usr/bin/python3
""" Task 2 module """


def append_write(filename="", text=""):
    """ append_write function that appends to a file """

    with open(filename, 'a+', encoding="utf-8") as f:

        res = f.write(text)

    return res
