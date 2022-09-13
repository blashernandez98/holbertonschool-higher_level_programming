#!/usr/bin/python3
def add_tuple(a=(), b=()):
    c = [0, 0]
    for i in range(0, 2):
        if (a is not None):
            if (len(a) > i):
                c[i] = a[i]
        if (b is not None):
            if (len(b) > i):
                c[i] += b[i]
    return (tuple(c))
