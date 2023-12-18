#!/usr/bin/python3
"""Test case for the user class"""
import unittest
from models.user import User  # Import the User class from your module
from datetime import datetime
import os
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
	"""Test case for the User class."""

	def setUp(self):
		"""Set up a User instance for testing."""
		self.user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")

	def tearDown(self):
		"""Clean up after the test."""
		del self.user

	def test_instance_creation(self):
		"""Test if the User instance is created correctly."""
		self.assertIsInstance(self.user, User)
		self.assertIsInstance(self.user, BaseModel)

	def test_attributes(self):
		"""Test if the User instance has the correct attributes."""
		self.assertEqual(self.user.email, "test@example.com")
		self.assertEqual(self.user.password, "password")
		self.assertEqual(self.user.first_name, "John")
		self.assertEqual(self.user.last_name, "Doe")

	def test_id_generation(self):
		"""Test if the User instance generates a valid ID."""
		self.assertTrue(hasattr(self.user, 'id'))
		self.assertIsInstance(self.user.id, str)

	def test_created_at_and_updated_at(self):
		"""Test if created_at and updated_at attributes are set correctly."""
		self.assertTrue(hasattr(self.user, 'created_at'))
		self.assertTrue(hasattr(self.user, 'updated_at'))
		self.assertIsInstance(self.user.created_at, datetime)
		self.assertIsInstance(self.user.updated_at, datetime)
		self.assertEqual(self.user.created_at, self.user.updated_at)

	def test_to_dict_method(self):
		"""Test the to_dict method of the User instance."""
		user_dict = self.user.to_dict()
		self.assertIsInstance(user_dict, dict)
		self.assertIn('id', user_dict)
		self.assertIn('email', user_dict)
		self.assertIn('password', user_dict)
		self.assertIn('first_name', user_dict)
		self.assertIn('last_name', user_dict)
		self.assertIn('created_at', user_dict)
		self.assertIn('updated_at', user_dict)
		self.assertEqual(user_dict['email'], "test@example.com")
		self.assertEqual(user_dict['password'], "password")
		self.assertEqual(user_dict['first_name'], "John")
		self.assertEqual(user_dict['last_name'], "Doe")

	def test_save_method(self):
		"""Test if the save method correctly saves the User instance."""
		self.user.save()
		file_path = "files/store.json"
		self.assertTrue(os.path.exists(file_path))
		with open(file_path, 'r') as file:
			content = file.read()
			self.assertIn("User." + self.user.id, content)


if __name__ == '__main__':
	unittest.main()

