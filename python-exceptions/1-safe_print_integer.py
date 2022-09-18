#!/usr/bin/python3


def safe_print_integer(integer_maybe):

    try:
        print("{:d}".format(integer_maybe))
        return True

    except (ValueError, TypeError):
        return False
