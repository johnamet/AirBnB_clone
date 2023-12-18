import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand  # Replace 'your_module_name' with the actual module name
import uuid
from models import storage
import os


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def tearDown(self):
        os.remove("files/store.json")

    def test_create_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            key = f"BaseModel.{output}"
            self.assertTrue(output)  # Check that output is not empty
            self.assertIn(key, storage.all().keys())

    def test_update_command(self):
        # Assuming an instance of BaseModel is created
        with patch('sys.stdout', new_callable=StringIO)as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            create_output = mock_stdout.getvalue().strip()

        # Extracting ID from create output
        obj_id = create_output.strip()
        key = f"BaseModel.{obj_id}"

        # Running the update command
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd(f'update BaseModel {obj_id} name "New Name"')
            update_output = mock_stdout.getvalue().strip()

        # Checking if the update was successful
        self.assertEqual(update_output, '')

        # Fetching the instance and checking the updated attribute
        updated_instance = storage.all().get(key)
        self.assertIsNotNone(updated_instance)
        self.assertEqual(updated_instance.name, "New Name")

    def test_all_command(self):
        # Assuming instances of BaseModel and User are created
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            self.hbnb_cmd.onecmd("create User")
            create_output = mock_stdout.getvalue().strip()

        # Running the all command
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd('all')
            all_output = mock_stdout.getvalue().strip()

        # Checking if both instances are in the output
        self.assertIn("BaseModel", all_output)
        self.assertIn("User", all_output)

    def test_destroy_command(self):
        # Assuming an instance of BaseModel is created
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            create_output = mock_stdout.getvalue().strip()

        # Extracting ID from create output
        obj_id = create_output.split()[-1]
        key = f"BaseModel.{obj_id}"

        # Running the destroy command
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd(f'destroy BaseModel {obj_id}')
            destroy_output = mock_stdout.getvalue().strip()

        # Checking if the destroy was successful
        self.assertEqual(destroy_output, '')

        # Fetching the instance and checking if it's deleted
        deleted_instance = self.hbnb_cmd.classes_dict["BaseModel"].__dict__.get(key)
        self.assertIsNone(deleted_instance)


if __name__ == '__main__':
    unittest.main()
