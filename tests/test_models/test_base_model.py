#!/usr/bin/python3
"""Test use cases of the BaseModel
"""

import unittest
from models.base_model import BaseModel
from models import storage
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Unit test  BaseModel method use cases
    """

    def setUp(self):
        """Set up unittest model """

        self.base_model = BaseModel()
        sleep(0.05)
        self.new_model = BaseModel()

    def test_uniq_id(self):
        self.assertNotEqual(self.new_model.id, self.base_model.id)

    def test_to_dict(self):
        _dict = self.base_model.to_dict()
        self.assertIn("id", _dict)
        self.assertIn("__class__", _dict)
        self.assertIn("created_at", _dict)
        self.assertIn("updated_at", _dict)

    def test_updated_at_on_save(self):
        """Test time on update"""

        prev_time = self.base_model.updated_at
        self.base_model.save()
        self.assertLess(prev_time, self.base_model.updated_at)

    def test_time_diff_in_created_at(self):
        """Test correctness of time of creation"""

        self.assertLess(
                self.base_model.created_at, self.new_model.created_at)

    def test_time_diff_in_updated_at(self):
        """Test successful update"""

        self.assertLess(
                self.base_model.updated_at, self.new_model.updated_at)

    def test_save(self):
        _id = f"{self.base_model.to_dict()['__class__']}.{self.base_model.id}"
        self.base_model.save()
        self.assertIn(_id, storage.all())


if __name__ == "__main__":
    unittest.main()
