#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first = None
    if (sentence is not None):
        length = len(sentence)
        if (length > 0):
            first = sentence[0]
    res = (length, first)
    return (res)
