#!/usr/bin/python3
def no_c(my_string):
    if (my_string is not None):
        new_string = ""
        for letter in my_string:
            if (letter != 'c' and letter != 'C'):
                new_string += letter
        return new_string
