#!/usr/bin/python3
""" Unittest for task 6 module  """


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """ Test class for max_integer function  """

    def test_start(self):
        self.assertEqual(max_integer([43, 41, 7]), 43)

    def test_middle(self):
        self.assertEqual(max_integer([2, 43, 7]), 43)

    def test_end(self):
        self.assertEqual(max_integer([2, 13, 43]), 43)

    def test_negative(self):
        self.assertEqual(max_integer([2, -43, 7]), 7)

    def test_all_negative(self):
        self.assertEqual(max_integer([-2, -43, -7]), -2)

    def test_single(self):
        self.assertEqual(max_integer([43]), 43)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
