#!/usr/bin/python3
"""This module is to the BaseModel class"""
from models.base_model import BaseModel
import unittest
import uuid
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Setup a BaseModel class"""
        self.model = BaseModel()
        storage.__objects = {}

    def test_base_model_creation(self):
        """Test the creation of a BaseModel instance."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(uuid.UUID(self.model.id), uuid.UUID)
        self.assertIsNotNone(self.model.created_at)
        self.assertIsNotNone(self.model.updated_at)
        self.assertEqual(self.model.created_at, self.model.updated_at)
        self.assertIsInstance(self.model.created_at, datetime)
    
    def test_base_model_with_kwargs(self):
        """Test the creation of a BaseModel instance using **kwargs."""
        self.model.example_attribute = "example_value"

        my_model = self.model.to_dict()

        base_model = BaseModel(**my_model)

        self.assertEqual(base_model.id, self.model.id)
        
        # Convert the string representation back to datetime for comparison
        created_at_datetime = datetime.fromisoformat(my_model["created_at"])
        updated_at_datetime = datetime.fromisoformat(my_model["updated_at"])

        self.assertEqual(base_model.created_at, created_at_datetime)
        self.assertEqual(base_model.updated_at, updated_at_datetime)
        
        self.assertEqual(base_model.example_attribute, self.model.example_attribute)


    def test_base_model_representation(self):
        """Test the __str__ method of the BaseModel class."""
        expected_str = "[BaseModel] ({}) \
                {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """Test the save method of the BaseModel class"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)


    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertIsInstance(model_dict["id"], str)
    


if __name__ == '__main__':
    unittest.main()
