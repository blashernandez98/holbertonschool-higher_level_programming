#!/usr/bin/python3
char = 122
for i in range(0, 26):
    print("{:c}".format(char), end='')
    if (i % 2 == 0):
        char -= 32
    else:
        char += 32
    char -= 1
