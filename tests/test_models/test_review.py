import unittest
from models.review import Review
import os

class TestReview(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Review class for testing
        self.review = Review(place_id="place_id_1", user_id="user_id_1", text="Great experience")

    def tearDown(self):
        # Clean up after the test
        del self.review

    def test_instance_creation(self):
        # Test if the Review instance is created correctly
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        # Test individual attributes
        self.assertEqual(self.review.place_id, "place_id_1")
        self.assertEqual(self.review.user_id, "user_id_1")
        self.assertEqual(self.review.text, "Great experience")

    def test_to_dict(self):
        # Test the to_dict method
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn("id", review_dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)
        self.assertEqual(review_dict["text"], "Great experience")

    def test_save_method(self):
        # Test if the save method correctly saves the Review instance
        self.review.save()
        file_path = "files/store.json"
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertIn("Review." + self.review.id, content)

if __name__ == "__main__":
    unittest.main()
