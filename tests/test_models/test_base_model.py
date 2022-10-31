#!/usr/bin/python3
"""Test use cases of the BaseModel
"""

import unittest
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Unit test  BaseModel method use cases
    """

    def setUp(self):
        self.base_model = BaseModel()
        sleep(0.05)
        self.new_model = BaseModel()

    def test_uniq_id(self):
        self.assertNotEqual(self.new_model.id, self.base_model.id)

    def test_updated_at_on_save(self):
        prev_time = self.base_model.updated_at
        self.base_model.save()
        self.assertLess(prev_time, self.base_model.updated_at)

    def test_time_diff_in_created_at(self):
        self.assertLess(
                self.base_model.created_at, self.new_model.created_at)

    def test_time_diff_in_updated_at(self):
        self.assertLess(
                self.base_model.updated_at, self.new_model.updated_at)


if __name__ == "__main__":
    unittest.main()
