import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the review model attributes"""
    def test_review_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")  # Default value for place_id
        self.assertEqual(review.user_id, "")  # Default value for user_id
        self.assertEqual(review.text, "")  # Default value for text


if __name__ == '__main__':
    unittest.main()
