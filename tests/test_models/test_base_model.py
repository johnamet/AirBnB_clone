#!/usr/bin/python3
"""This module is to the BaseModel class"""
from models.base_model import BaseModel
import unittest
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Setup a BaseModel class"""
        self.model = BaseModel()

    def test_base_model_creation(self):
        """Test the creation of a BaseModel instance."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(uuid.UUID(self.model.id), uuid.UUID)
        self.assertIsNotNone(self.model.created_at)
        self.assertIsNotNone(self.model.updated_at)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_base_model_with_id(self):
        """Test the creation of a BaseModel instance with a specified ID."""
        custom_id = "custom_id"
        base_model = BaseModel(id=custom_id)
        self.assertEqual(base_model.id, custom_id)

    def test_base_model_representation(self):
        """Test the __str__ method of the BaseModel class."""
        expected_str = "[BaseModel] ({}) \
                {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """Test the save method of the BaseModel class"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(
                datetime.fromisoformat(model_dict["created_at"]), datetime)
        self.assertIsInstance(
                datetime.fromisoformat(model_dict["updated_at"]), datetime)
        self.assertIsInstance(model_dict["id"], str)


if __name__ == '__main__':
    unittest.main()
