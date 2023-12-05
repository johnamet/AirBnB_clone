#!/usr/bin/python3
"""Test cases for the BaseModel class."""
import unittest
from models import storage
from models.base_model import BaseModel


class TestBaseModelStorage(unittest.TestCase):
    """Test cases for BaseModel storage interactions."""

    def setUp(self):
        """Setup a BaseModel class and clear the storage."""
        self.model = BaseModel()
        storage.__objects = {}

    def test_new_instance_added_to_storage(self):
        """Test that a new instance of BaseModel is added to the storage."""
        # Check that the storage is initially empty
        self.assertEqual(len(storage.all()), 0)

        # Create a new instance of BaseModel
        new_model = BaseModel()

        # Check that the new instance is added to the storage
        self.assertEqual(len(storage.all()), 1)
        key = "{}.{}".format(new_model.__class__.__name__, new_model.id)
        self.assertIn(key, storage.all())

        # Check that the stored instance is the same as the created instance
        stored_instance = storage.all()[key]
        self.assertIs(new_model, stored_instance)

    def test_existing_instance_not_added_to_storage(self):
        """Test that an existing instance of BaseModel is not added to the storage."""
        # Check that the storage is initially empty
        self.assertEqual(len(storage.all()), 0)

        # Create a new instance of BaseModel
        new_model = BaseModel()

        # Check that the new instance is added to the storage
        self.assertEqual(len(storage.all()), 1)
        key = "{}.{}".format(new_model.__class__.__name__, new_model.id)
        self.assertIn(key, storage.all())

        # Create another instance with the same ID
        duplicate_model = BaseModel(id=new_model.id)

        # Check that the duplicate instance is not added to the storage
        self.assertEqual(len(storage.all()), 1)
        self.assertNotIn(key, storage.all())

    def test_reload_method(self):
        """Test that the reload method properly loads instances into storage."""
        # Create a new instance of BaseModel
        new_model = BaseModel()

        # Save the storage to a file
        storage.save()

        # Clear the storage
        storage.__objects = {}

        # Reload the storage
        storage.reload()

        # Check that the reloaded instance is in the storage
        key = "{}.{}".format(new_model.__class__.__name__, new_model.id)
        self.assertIn(key, storage.all())
        reloaded_instance = storage.all()[key]
        self.assertIs(new_model, reloaded_instance)


if __name__ == '__main__':
    unittest.main()
