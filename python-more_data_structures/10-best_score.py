#!/usr/bin/python3


def best_score(dic):
    score = 0

    if dic is not None:

        for key, value in dic.items():
            if value > score:
                key_candidate = key
                score = value

        return key_candidate

    else:
        return None
