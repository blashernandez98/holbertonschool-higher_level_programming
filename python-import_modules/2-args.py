#!/usr/bin/python3
if (__name__ == '__main__'):
    import sys
    argc = len(sys.argv) - 1
    print("{:d} argument".format(argc), end='')
    if (argc == 0):
        print("s.")
        quit()
    if (argc == 1):
        print(":")
    else:
        print("s:")
    for i in range(1, argc + 1):
        print("{:d}: {}".format(i, sys.argv[i]))
