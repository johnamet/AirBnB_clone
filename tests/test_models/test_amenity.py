import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")  # Default value for name

if __name__ == '__main__':
    unittest.main()
