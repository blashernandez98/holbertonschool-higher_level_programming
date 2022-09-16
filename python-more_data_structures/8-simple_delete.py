#!/usr/bin/python3


def simple_delete(dic, key):
    if dic is not None:
        if key in dic.keys():
            del dic[key]

    return dic
