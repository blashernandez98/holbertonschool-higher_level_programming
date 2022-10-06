#!/usr/bin/python3
""" Tests module for Base Class """
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """ TestBase class """

    def setUp(self):
        self.base = Base()

    def test_id(self):
        self.assertEqual(str(type(self.base)), "<class 'models.base.Base'>")
