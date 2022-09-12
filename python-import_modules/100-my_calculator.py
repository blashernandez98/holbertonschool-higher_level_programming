#!/usr/bin/python3
if (__name__ == '__main__'):
    from calculator_1 import *
    import sys
    argv = sys.argv
    argc = len(argv)
    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    operators = [["+", add], ["-", sub], ["*", mul], ["/", div]]
    for op in operators:
        if (argv[2] == op[0]):
            print("{:d} {} {:d} = {:d}".format(a, op[0], b, op[1](a, b)))
            quit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    quit(1)
