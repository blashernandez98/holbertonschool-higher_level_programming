#!/usr/bin/python3
def print_matrix_integer(matrix = [[]]):
    if (matrix is not None):
        for row in matrix:
            for i in range(len(row)):
                print("{:d}".format(element), end="")
                if (i != len(row) - 1):
                    print("", end=" ")
            print("")
