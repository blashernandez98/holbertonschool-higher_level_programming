#!/usr/bin/python3


def complex_delete(dic, value):

    del_keys = []

    for key, val in dic.items():

        if (val == value):
            del_keys.append(key)

    for key in del_keys:
        del dic[key]

    return dic
