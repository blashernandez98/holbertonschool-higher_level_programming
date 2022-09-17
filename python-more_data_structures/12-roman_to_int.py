#!/usr/bin/python3


def roman_to_int(roman):
    res, i = 0, 0
    if roman is not None and type(roman) == str:
        dic = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        last = len(roman) - 1

        for i in range(0, last + 1):
            if (i < last and dic.get(roman[i]) < dic.get(roman[i+1])):

                res -= dic.get(roman[i])
            else:
                res += dic.get(roman[i])

    return res
