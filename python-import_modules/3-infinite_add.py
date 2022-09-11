#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    argc = len(sys.argv)
    a = 0
    for i in range(1, argc):
        a += int(sys.argv[i])
    print(a)
