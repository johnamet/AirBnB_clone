import unittest
from models.amenity import Amenity
import os

class TestAmenity(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Amenity class for testing
        self.amenity = Amenity(name="Swimming Pool")

    def tearDown(self):
        # Clean up after the test
        del self.amenity

    def test_instance_creation(self):
        # Test if the Amenity instance is created correctly
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        # Test individual attributes
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_to_dict(self):
        # Test the to_dict method
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("id", amenity_dict)
        self.assertIn("name", amenity_dict)
        self.assertEqual(amenity_dict["name"], "Swimming Pool")

    def test_save_method(self):
        # Test if the save method correctly saves the Amenity instance
        self.amenity.save()
        file_path = "files/store.json"
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertIn("Amenity." + self.amenity.id, content)

if __name__ == "__main__":
    unittest.main()
