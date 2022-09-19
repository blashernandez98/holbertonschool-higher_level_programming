#!/usr/bin/python3


def weight_average(my_list):

    weighted = [0, 0]

    if my_list is None or len(my_list) == 0:
        return 0

    for index, tup in enumerate(my_list):

        weighted[0] += tup[0] * tup[1]
        weighted[1] += tup[1]

    return (weighted[0] / weighted[1])
