#!/usr/bin/python3
""" Task 5 module """


def text_indentation(text):
    """ Text indentation function  """

    if type(text) is not str:
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    new_l = True

    for letter in text:

        if new_l and letter == ' ':
            continue

        new_l = False

        print(letter, end="")

        if letter in separators:
            print('\n' * 2)
            new_l = True
            continue
