#!/usr/bin/python3
"""Unit test State module"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test state instance """

    def setUp(self):
        """Set up State test case"""

        self.place = Place()

    def test_inheritance(self):
        """Test if is instance of BaseModel """

        self.assertIsInstance(self.place, BaseModel)

    def test_init(self):
        """Verify instance"""

        self.assertIsInstance(self.place, Place)
