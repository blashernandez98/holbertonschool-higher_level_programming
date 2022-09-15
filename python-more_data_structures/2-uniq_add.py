#!/usr/bin/python3

def uniq_add(my_list):
    uniques, res = [], 0

    if my_list is not None:

        for element in my_list:
            if element not in uniques:
                uniques.append(element)

        for n in uniques:
            res += n

    else:
        return None

    return res
