#!/usr/bin/python3
if (__name__ == '__main__'):
    from calculator_1 import *
    import sys
    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    argv = sys.argv
    argc = len(argv)
    a = int(argv[1])
    b = int(argv[3])
    operators = [["+", add], ["-", sub], ["*", mul], ["/", div]]
    for i in range(0, 4):
        if (argv[2] == operators[i][0]):
            print("{:d} {} {:d} = {:d}".format(a, operators[i][0], b, operators[i][1](a, b)))
            quit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    quit(1)
