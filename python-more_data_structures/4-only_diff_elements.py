#!/usr/bin/python3


def only_diff_elements(set1, set2):
    if all(s is not None for s in (set1, set2)):

        return (set1.symmetric_difference(set2))
