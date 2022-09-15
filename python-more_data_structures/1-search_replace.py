#!/usr/bin/python3
def search_replace(my_list, search, replace):

    new_list = []

    if my_list is not None:

        new_list = list(map(lambda e: replace if e == search else e, my_list))

    else:
        return None

    return (new_list)
