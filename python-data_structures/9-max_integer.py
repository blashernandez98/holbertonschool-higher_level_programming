#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list is not None and len(my_list)):
        big = 0
        for number in my_list:
            if (number > big):
                big = number
        return big
    else:
        return None
