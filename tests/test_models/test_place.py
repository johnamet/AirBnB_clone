import unittest
from models.place import Place
import os

class TestPlace(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Place class for testing
        self.place = Place(city_id="city_id_1", user_id="user_id_1", name="Cozy Cottage")

    def tearDown(self):
        # Clean up after the test
        del self.place

    def test_instance_creation(self):
        # Test if the Place instance is created correctly
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        # Test individual attributes
        self.assertEqual(self.place.city_id, "city_id_1")
        self.assertEqual(self.place.user_id, "user_id_1")
        self.assertEqual(self.place.name, "Cozy Cottage")

    def test_to_dict(self):
        # Test the to_dict method
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn("id", place_dict)
        self.assertIn("city_id", place_dict)
        self.assertIn("user_id", place_dict)
        self.assertIn("name", place_dict)
        self.assertEqual(place_dict["name"], "Cozy Cottage")

    def test_save_method(self):
        # Test if the save method correctly saves the Place instance
        self.place.save()
        file_path = "files/store.json"
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertIn("Place." + self.place.id, content)

if __name__ == "__main__":
    unittest.main()
