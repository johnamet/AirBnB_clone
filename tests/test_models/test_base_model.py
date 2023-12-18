#!/usr/bin/python3
"""Test case for the base model"""
import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test the attributes and methods of the BaseModel"""

    def setUp(self):
        """Set up an instance of the BaseModel for testing"""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after the test"""
        del self.model

    def test_instance_saved_in_storage(self):
        """Test whether the instance is saved in the storage"""
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, storage.all())

    def test_id_not_empty_or_none(self):
        """Test that the id is not empty or None"""
        self.assertIsNotNone(self.model.id)
        self.assertNotEqual(self.model.id, "")

    def test_attribute_update(self):
        """Test the update of instance attributes"""
        self.model.name = "First BaseModel"
        self.model.save()
        # Check whether the new attribute has been added
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "First BaseModel")
    
    def test_duplicate_instance_creation(self):
        # create new instance from old
        old_dict = self.model.to_dict()
        new_model = BaseModel(**old_dict)
        self.model.just_attr = "Test 123"
        new_model.save()

        # load the new instance from json
        key = "BaseModel.{}".format(new_model.id)
        loaded_model = storage.all()[key]

        self.assertTrue(hasattr(loaded_model, "just_attr"))
        self.assertEqual(loaded_model.just_attr, "Test 123")

    def test_datetime_update(self):
        """Test whether the updated_at attribute gets updated"""
        initial_updated_at = self.model.updated_at
        self.model.new_attr = "New New"
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)

    def test_save_method(self):
        """Test the save method"""
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    def test_str_representation(self):
        """Test the __str__ representation of the model"""
        str_representation = str(self.model)
        self.assertIn("BaseModel", str_representation)
        self.assertIn(str(self.model.id), str_representation)

    def test_kwargs_initialization(self):
        """Test instance initialization with keyword arguments"""
        new_model = BaseModel(id="test_id", created_at="2022-01-01T00:00:00",
                              updated_at="2022-01-01T00:00:00")
        self.assertEqual(new_model.id, "test_id")
        self.assertEqual(new_model.created_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(new_model.updated_at.isoformat(), "2022-01-01T00:00:00")


if __name__ == "__main__":
    unittest.main()
