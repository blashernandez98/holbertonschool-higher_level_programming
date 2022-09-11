#!/usr/bin/python3
def uppercase(str):
    islower = 0
    for letter in str:
        if (ord(letter) > 96 and ord(letter) < 123):
            islower = 32
        else:
            islower = 0

        print("{:c}".format(ord(letter) - islower), end="")
    print()
