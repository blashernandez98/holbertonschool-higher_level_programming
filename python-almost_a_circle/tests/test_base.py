#!/usr/bin/python3
""" Tests module for Base Class """
import unittest
from models.base import Base


class testBaseClass(unittest.TestCase):
    """ TestBase class """

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id2(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    if __name__ == "__main__":
        unittest.main()
