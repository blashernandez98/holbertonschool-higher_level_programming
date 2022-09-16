#!usr/bin/python3


def multiply_by_2(dic):
    new_dic = {}

    if dic is not None:

        for key, value in dic.items():
            new_dic[key] = value*2

    return new_dic
