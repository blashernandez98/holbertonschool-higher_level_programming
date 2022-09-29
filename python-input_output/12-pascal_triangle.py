#!/usr/bin/python3
""" Pascal triangle maker - Task 12 """


def pascal_triangle(n):
    """ pascal_triangle func that returns pascal triangle of size n """

    if n == 0:
        return []

    pascal = [[1]]

    for i in range(n - 1):

        row = [1]
        j = 1

        while (j < len(pascal[i]) + 1):

            row.append(pascal[i][j - 1])

            try:
                row[j] += pascal[i][j]

            except IndexError:
                pass

            j += 1

        pascal.append(row)

    return pascal
