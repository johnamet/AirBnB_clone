#!/usr/bin/python3
"""Test case for multiple instances of different models"""
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

class TestMultipleInstances(unittest.TestCase):
    """Test case for multiple instances of different models."""

    def setUp(self):
        """Set up the FileStorage instance for testing."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after the test."""
        del self.storage

    def test_multiple_instances_creation(self):
        """Test creating and managing multiple instances."""
        # Create instances for different models
        user1 = User(email="user1@example.com", password="password1")
        user2 = User(email="user2@example.com", password="password2")
        city1 = City(state_id="state_id_1", name="City1")
        city2 = City(state_id="state_id_2", name="City2")
        amenity1 = Amenity(name="Amenity1")
        amenity2 = Amenity(name="Amenity2")
        state1 = State(name="State1")
        state2 = State(name="State2")
        review1 = Review(place_id="place_id_1", user_id="user_id_1", text="Review1")
        review2 = Review(place_id="place_id_2", user_id="user_id_2", text="Review2")
        place1 = Place(city_id="city_id_1", user_id="user_id_1", name="Place1")
        place2 = Place(city_id="city_id_2", user_id="user_id_2", name="Place2")

        # Add instances to the FileStorage and save
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.new(city1)
        self.storage.new(city2)
        self.storage.new(amenity1)
        self.storage.new(amenity2)
        self.storage.new(state1)
        self.storage.new(state2)
        self.storage.new(review1)
        self.storage.new(review2)
        self.storage.new(place1)
        self.storage.new(place2)
        self.storage.save()

        # Reload the storage and check if all instances are present
        new_storage = FileStorage()
        new_storage.reload()

        # Check users
        self.assertIn(f"User.{user1.id}", new_storage.all())
        self.assertIn(f"User.{user2.id}", new_storage.all())

        # Check cities
        self.assertIn(f"City.{city1.id}", new_storage.all())
        self.assertIn(f"City.{city2.id}", new_storage.all())

        # Check amenities
        self.assertIn(f"Amenity.{amenity1.id}", new_storage.all())
        self.assertIn(f"Amenity.{amenity2.id}", new_storage.all())

        # Check states
        self.assertIn(f"State.{state1.id}", new_storage.all())
        self.assertIn(f"State.{state2.id}", new_storage.all())

        # Check reviews
        self.assertIn(f"Review.{review1.id}", new_storage.all())
        self.assertIn(f"Review.{review2.id}", new_storage.all())

        # Check places
        self.assertIn(f"Place.{place1.id}", new_storage.all())
        self.assertIn(f"Place.{place2.id}", new_storage.all())

if __name__ == '__main__':
    unittest.main()
