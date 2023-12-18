import unittest
from models.city import City
import os

class TestCity(unittest.TestCase):
    def setUp(self):
        # Create an instance of the City class for testing
        self.city = City(state_id="state_id_1", name="San Francisco")

    def tearDown(self):
        # Clean up after the test
        del self.city

    def test_instance_creation(self):
        # Test if the City instance is created correctly
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        # Test individual attributes
        self.assertEqual(self.city.state_id, "state_id_1")
        self.assertEqual(self.city.name, "San Francisco")

    def test_to_dict(self):
        # Test the to_dict method
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn("id", city_dict)
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)
        self.assertEqual(city_dict["name"], "San Francisco")

    def test_save_method(self):
        # Test if the save method correctly saves the City instance
        self.city.save()
        file_path = "files/store.json"
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertIn("City." + self.city.id, content)

if __name__ == "__main__":
    unittest.main()
