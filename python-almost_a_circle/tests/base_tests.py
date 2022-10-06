#!/usr/bin/python3
""" Tests module for Base Class """
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ TestBase class """

    def test_id(self):
        base = Base()
        self.assertEqual(base.id, 1)
