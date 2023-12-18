import unittest
from models.state import State
import os

class TestState(unittest.TestCase):
    def setUp(self):
        # Create an instance of the State class for testing
        self.state = State(name="California")

    def tearDown(self):
        # Clean up after the test
        del self.state

    def test_instance_creation(self):
        # Test if the State instance is created correctly
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        # Test individual attributes
        self.assertEqual(self.state.name, "California")

    def test_to_dict(self):
        # Test the to_dict method
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("id", state_dict)
        self.assertIn("name", state_dict)
        self.assertEqual(state_dict["name"], "California")

    def test_save_method(self):
        # Test if the save method correctly saves the State instance
        self.state.save()
        file_path = "files/store.json"
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertIn("State." + self.state.id, content)

if __name__ == "__main__":
    unittest.main()
