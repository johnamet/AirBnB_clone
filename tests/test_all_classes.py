#!/usr/bin/python3
"""Combined test case for all models"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage

class TestAllModels(unittest.TestCase):
    """Combined test case for all models."""

    def setUp(self):
        """Set up the FileStorage instance for testing."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after the test."""
        del self.storage

    def test_base_model(self):
        """Test the BaseModel class and its interaction with FileStorage."""
        model = BaseModel()
        key = f"{model.__class__.__name__}.{model.id}"

        # Test new, save, and reload methods
        self.storage.new(model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(key, new_storage.all())
        loaded_model = new_storage.all()[key]
        self.assertIsInstance(loaded_model, BaseModel)

    def test_user_model(self):
        """Test the User class and its interaction with FileStorage."""
        user = User(email="test@example.com", password="password")
        key = f"{user.__class__.__name__}.{user.id}"

        # Test new, save, and reload methods
        self.storage.new(user)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(key, new_storage.all())
        loaded_user = new_storage.all()[key]
        self.assertIsInstance(loaded_user, User)

    def test_city_model(self):
        """Test the City class and its interaction with FileStorage."""
        city = City(state_id="state_id_1", name="City Name")
        key = f"{city.__class__.__name__}.{city.id}"

        # Test new, save, and reload methods
        self.storage.new(city)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(key, new_storage.all())
        loaded_city = new_storage.all()[key]
        self.assertIsInstance(loaded_city, City)

    # Add similar test methods for Amenity, State, Review, and Place models

    def test_save_file_exists(self):
        """Test if the save method creates a file."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        file_path = "files/store.json"
        self.assertTrue(os.path.exists(file_path))

    

if __name__ == '__main__':
    unittest.main()
