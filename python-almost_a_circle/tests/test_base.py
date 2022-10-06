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
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id3(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    # def test_to_json(self):
    #    b1 = Base()
    #    self.assertEqual(b1.to_json_string(), "")
