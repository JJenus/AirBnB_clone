#!/usr/bin/python3
"""Unit test State module"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test state instance """

    def setUp(self):
        """Set up State test case"""

        self.amenity = Amenity()

    def test_inheritance(self):
        """Test if is instance of BaseModel """

        self.assertIsInstance(self.amenity, BaseModel)

    def test_init(self):
        """Verify instance"""

        self.assertIsInstance(self.amenity, Amenity)
