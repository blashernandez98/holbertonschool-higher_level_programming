#!/usr/bin/python3
""" Task 0 module """


def read_file(filename=""):

    with open(filename, encoding="utf-8") as f:

        file_content = f.read()

    print(file_content)
