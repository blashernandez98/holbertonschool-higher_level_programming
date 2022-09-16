#!/usr/bin/python3


def print_sorted_dictionary(dic):

    if dic is not None:
        sorted_keys = sorted(dic.keys())
        for key in sorted_keys:
            print(f"{key}: {dic[key]}")
