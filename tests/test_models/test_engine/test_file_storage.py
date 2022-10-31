#!/usr/bin/python3
""" File storage unit test module """

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test file storage"""

    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        model = BaseModel()
        key = f"{type(model).__name__}.{model.id}"
        self.storage.new(model)
        objs = self.storage.all()
        self.assertIsNotNone(objs[key])

    def test_save(self):
        self.assertIsNone(self.storage.save())

    def test_reload(self):
        """Fix reload test"""
        self.assertIsNone(self.storage.reload())
