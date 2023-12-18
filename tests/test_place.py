import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test the attributes of the placd model"""
    def test_place_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")  # Default value for city_id
        self.assertEqual(place.user_id, "")  # Default value for user_id
        self.assertEqual(place.name, "")  # Default value for name
        # Add more assertions for other attributes


if __name__ == '__main__':
    unittest.main()
