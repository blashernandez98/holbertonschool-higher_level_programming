#!/usr/bin/python3
""" Task 100 module """


def append_after(filename="", search_string="", new_string=""):

    output = ""

    with open(filename, 'r+', encoding="utf-8") as f:

        for line in f:

            output += line

            if search_string in line:

                output += new_string

    with open(filename, 'w+', encoding="utf-8") as f:

        f.write(output)
