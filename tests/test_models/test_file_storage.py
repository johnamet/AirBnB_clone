#!/usr/bin/python3
"""Test case for the FileStorage class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place

class TestFileStorage(unittest.TestCase):
    """Test case for the FileStorage class."""

    def setUp(self):
        """Set up the FileStorage instance for testing."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after the test."""
        del self.storage

    def test_default_attributes(self):
        """Test the default attributes of the FileStorage instance."""
        self.assertEqual(self.storage._FileStorage__file_path, "files/store.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_method(self):
        """Test the all method of the FileStorage instance."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, self.storage._FileStorage__objects)

    def test_delete_method(self):
        """Test the delete method of the FileStorage instance."""
        model = BaseModel()
        self.storage.new(model)
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, self.storage.all())
        self.storage.delete(model)
        self.assertNotIn(key, self.storage.all())

    def test_new_method(self):
        """Test the new method of the FileStorage instance."""
        model = User()
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertNotIn(key, self.storage.all())
        self.storage.new(model)
        self.assertIn(key, self.storage.all())

    def test_save_and_reload_methods(self):
        """Test the save and reload methods of the FileStorage instance."""
        model = BaseModel()
        key = f"{model.__class__.__name__}.{model.id}"
        self.storage.new(model)
        self.storage.save()

        # Reload the storage and check if the model is present
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(key, new_storage.all())
        loaded_model = new_storage.all()[key]
        self.assertIsInstance(loaded_model, BaseModel)

    def test_save_reload_with_multiple_objects(self):
        """Test save and reload methods with multiple objects."""
        user = User(email="user@example.com", password="password")
        base_model = BaseModel()
        self.storage.new(user)
        self.storage.new(base_model)
        self.storage.save()
        self.storage.reload()
        user_key = f"{user.__class__.__name__}.{user.id}"
        base_model_key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(user_key, self.storage.all())
        self.assertIn(base_model_key, self.storage.all())
        
    def test_save_file_exists(self):
        """Test if the save method creates a file."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        file_path = "files/store.json"
        self.assertTrue(os.path.exists(file_path))

if __name__ == '__main__':
    unittest.main()
