#!/usr/bin/python3
for first_d in range(0, 9):
    for second_d in range(1, 10):
        if (first_d == 8):
            continue
        print("{:d}".format(first_d), end="")
        print("{:d}".format(second_d), end=", ")
print("89")
