#!/usr/bin/python3
"""Unit test State module"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test state instance """

    def setUp(self):
        """Set up State test case"""

        self.state = State()

    def test_inheritance(self):
        """Test if is instance of BaseModel """

        self.assertIsInstance(self.state, BaseModel)

    def test_init(self):
        """Verify instance"""

        self.assertIsInstance(self.state, State)
