#!/usr/bin/python3
""" Unittest for task 6 module  """


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """ Test class for max_integer function  """

    def test_simple(self):
        self.assertEqual(max_integer([2, 43, 7]), 43)


if __name__ == '__main__':
    unittest.main()
