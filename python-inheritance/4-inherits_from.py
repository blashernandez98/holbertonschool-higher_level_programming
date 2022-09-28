#!/usr/bin/python3
""" Task 4 module """


def inherits_from(obj, a_class):
    """ inherits_from fuction """

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
