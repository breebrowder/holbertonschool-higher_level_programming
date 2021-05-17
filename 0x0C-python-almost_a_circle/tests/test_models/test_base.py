#!/usr/bin/python3
""" UNITTEST """
import unittest
from models.base import Base


class TestBase(unitest.TestCase):

    def test(self):
        self.assertEqual(Base(), 1)
