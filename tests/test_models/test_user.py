import unittest
from models.user import User
from datetime import datetime


class TestUserClass(unittest.TestCase):
    """Test cases for the User class."""

    def test_user_creation(self):
        """Test creating a User instance."""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test setting and accessing attributes of User."""
        user = User()
        user.username = "test_user"
        user.email = "test@example.com"
        user.password = "test_password"
        user.created_at = datetime.now()
        user.updated_at = datetime.now()

        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "test_password")

    def test_user_str_representation(self):
        """Test the string representation of User."""
        user = User()
        user.username = "test_user"
        user.email = "test@example.com"
        user.password = "test_password"

        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

        
if __name__ == '__main__':
    unittest.main()

