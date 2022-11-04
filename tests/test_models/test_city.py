#!/usr/bin/python3
"""Unit test State module"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test state instance """

    def setUp(self):
        """Set up State test case"""

        self.city = City()

    def test_inheritance(self):
        """Test if is instance of BaseModel """

        self.assertIsInstance(self.city, BaseModel)

    def test_init(self):
        """Verify instance"""

        self.assertIsInstance(self.city, City)
