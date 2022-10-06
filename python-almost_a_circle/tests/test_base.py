#!/usr/bin/python3
""" Tests module for Base Class """
import unittest
from models.base import Base


class testBaseClass(unittest.TestCase):
    """ TestBase class """

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
