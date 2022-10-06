#!/usr/bin/python3
""" Square class tests module """

from models.square import Square
import unittest


class testSquareClass(unittest.TestCase):
    """ Test Square class """

    def test_square_0(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        s1 = Square(1, 2)
        self.assertEqual(s1.x, 2)
        s1 = Square(1, 2, 3)
        self.assertEqual(s1.y, 3)

    def test_square_errors(self):
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "1")
        self.assertRaises(TypeError, Square, 1, 1, "1")
        self.assertRaises(TypeError, Square, 1, 2, 3, 4)
        self.assertRaises(TypeError, Square, -1)
        self.assertRaises(TypeError, Square, 1, -1)
        self.assertRaises(TypeError, Square, 1, 1, -43)
        self.assertRaises(ValueError, Square, 0)
