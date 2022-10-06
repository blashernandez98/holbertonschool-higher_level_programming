#!/usr/bin/python3
""" Rectangle class test module """
import unittest
from models.rectangle import Rectangle


class testRectangleClass(unittest.TestCase):
    """ Test Rectangle class """

    def test_rectangle(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        r1 = Rectangle(1, 2, 3, 4, 43)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.area(), 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (43) 3/4 - 1/2")

    def test_rectangle_errors(self):
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "43")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "43")
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)
