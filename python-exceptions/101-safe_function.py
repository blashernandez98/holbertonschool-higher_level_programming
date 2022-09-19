#!/usr/bin/python3


def safe_function(func, *args):

    try:
        res = func(*args)
        return res

    except Exception as err:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
        return None
