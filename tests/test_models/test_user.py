#!/usr/bin/python3
"""Unit test user """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unit test User instance"""

    def setUp(self):
        self.user = User()
        self.user.email = "great@kw.com"
        self.user.last_name = "mathew"
        self.user.first_name = "Mayokun"
        self.user.password = "secrete"

    def test_inheritance(self):
        _dict = self.user.to_dict()
        self.assertIn("id", _dict)
        self.assertIn("__class__", _dict)
        self.assertIn("created_at", _dict)
        self.assertIn("updated_at", _dict)

    def test_init(self):
        self.assertIn("email", self.user.to_dict())
        self.assertIn("password", self.user.to_dict())
        self.assertIn("first_name", self.user.to_dict())
        self.assertIn("last_name", self.user.to_dict())

    def test_instance(self):
        self.assertIsInstance(self.user, User)
