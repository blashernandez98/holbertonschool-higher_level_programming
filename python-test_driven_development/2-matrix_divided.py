#!/usr/bin/python3
""" Task 2 module  """


def matrix_divided(matrix, div):
    """ Matrix division function  """

    type_error = False
    n_rows = 0
    n_elements = 0

    if matrix is None or type(matrix) is not list:
        type_error = True
    else:
        for row in matrix:
            if type(row) is not list:
                type_error = True
                break
            else:
                n_rows += 1

            for n in row:
                if (type(n) is not float and type(n) is not int):
                    type_error = True
                    break
                else:
                    n_elements += 1

    if (type_error):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if (n_rows != n_elements / n_rows):
        raise TypeError("Each row of the matrix must have the same size")
    if (div is None or (type(div) is not int and type(div) is not float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    return (list(map(lambda x:
            list(map(lambda y: round(y / div, 2), x)), matrix)))
