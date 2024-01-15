#!/usr/bin/python3
"""Defines a class BaseModelTest"""


import json
import unittest
import os
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """ Defines tests for Base class """

    def setUp(self):
        """ Runs for each test """
        Base._Base__nb_objects = 0
        self.new_base = Base(id=1)

    def tearDown(self):
        """ Cleans up after each test """
        pass

    def test_check_instance_variables(self):
        """ Checks instance variables """
        self.assertEqual(self.new_base.id, 1)

    def test_docstring(self):
        """ Test if docstring is present """
        self.assertIsNotNone(Base.__doc__)

    def test_randos_id(self):
        """ Test random arguments passed """
        test1 = Base(7)
        self.assertEqual(test1.id, 7)
        test2 = Base(24)
        self.assertEqual(test2.id, 24)
        test3 = Base()
        self.assertEqual(test3.id, 1)
        test4 = Base(-24)
        self.assertEqual(test4.id, -24)

    def test_consecutive_ids(self):
        """ Tests consecutive ids """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_0_id(self):
        """ Test id to see if it duplicates """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_constructor(self):
        """ Tests constructor signature """
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_constructor_args_2(self):
        """ Tests constructor signature with 2 notself args """
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

