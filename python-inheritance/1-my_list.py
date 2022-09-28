#!/usr/bin/python3
""" Task 1 module  """


class MyList(list):
    """ Mylist class  """

    def print_sorted(self):
        """ Print sorted list method  """

        new_list = self[:]
        new_list.sort()
        print(new_list)
