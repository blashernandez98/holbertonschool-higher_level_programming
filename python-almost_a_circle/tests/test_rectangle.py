#!/usr/bin/python3
""" Rectangle class test module """
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


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
        dic = {'id': 43, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r1.to_dictionary(), dic)

    def test_rectangle_update(self):
        r1 = Rectangle(2, 2)
        r1.update()
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_rectangle_create(self):
        dic = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dic)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

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

    def test_rectangle_display(self):
        captured_out = StringIO()
        sys.stdout = captured_out
        r_no_pos = Rectangle(1, 1)
        r_no_pos.display()
        self.assertEqual(captured_out.getvalue(), '#\n')
        sys.stdout = sys.__stdout__

    def test_rectangle_display2(self):
        captured_out = StringIO()
        sys.stdout = captured_out
        r_with_pos = Rectangle(1, 1, 1, 1)
        r_with_pos.display()
        self.assertEqual(captured_out.getvalue(), '\n #\n')
        sys.stdout = sys.__stdout__
