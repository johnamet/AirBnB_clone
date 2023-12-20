#!/usr/bin/python3
"""The module contains one class, `HBNBCommand`
   This is to manage the objects of the AirBnB project
"""
import ast
import re
import cmd 
from io import StringIO
from typing import IO, List

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """The console is to manage the objects of the AirBnB clone project."""

    prompt = "(hbnb) "
    classes_dict = {"BaseModel": BaseModel, "User": User,
                    "City": City, "Amenity": Amenity, "Place": Place,
                    "Review": Review, "State": State}

    def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None) -> None:
        super().__init__(completekey, stdin, stdout)
        self._original_stdout = stdout  # Save the original stdout

    def clear_output(self) -> None:
        """Clear the standard output."""
        self.stdout = StringIO()  # Replace stdout with a new empty StringIO

    def restore_output(self) -> None:
        """Restore the original standard output."""
        self.stdout = self._original_stdout  # Restore the original stdout

    def default(self, line: str) -> None:
        """Handle commands in the form <model>.<command>."""
        if "." in line:
            model, command = line.split(".", 1)
            if model in self.classes_dict:
                self._handle_model_command(model, command)
            else:
                print("** class doesn't exist **")
        else:
            super().default(line)

    def _handle_model_command(self, model: str, command: str) -> None:
        """Handle commands specific to a model."""
        if command == "all()":
            self._do_all(model)
        elif command == "count()":
            print(self._do_count(model))
        elif "show" in command:
            pattern = r'show\("([^"]+)"\)'
            match = re.search(pattern, command)
            if match:
                id = match.group(1)
                self._do_show(model, id)
            else:
                print("** invalid command syntax for show **")
        elif "destroy" in command:
            pattern = r'destroy\("([^"]+)"\)'
            match = re.search(pattern, command)
            if match:
                id = match.group(1)
                self._do_destroy(model, id)
            else:
                print("** invalid command syntax for destroy **")
        elif "update" in command:
            # Define the regex pattern
            pattern = r'update\("([^"]+)",\s*({[^}]+})\)'
            # Use re.search to find the match
            match = re.search(pattern, command)
            if match:
                obj_id = match.group(1)
                obj_dict = match.group(2)

                if not obj_id:
                    print("** instance id missing **")
                if model not in self.classes_dict:
                    print("** class doesn't exist **")
                key = "{}.{}".format(model, obj_id)

                if key not in storage.all().keys():
                    print("** instance not found **")
                elif not obj_dict:
                    print("** dictionary missing **")
                else:
                    self._do_update(key, obj_dict)
            else:
                print("** invalid command syntax for update **")
        else:
            print(f"** Unknown command: {model}.{command} **")

    def _do_all(self, model: str) -> None:
        """Print all string representations of instances based on the class."""
        all_obj = storage.all()
        cls_list = [str(value) for key, value in all_obj.items()
                    if model in key]
        print(cls_list)

    def _do_count(self, model: str) -> int:
        """Count all instances of `model` """
        all_obj = storage.all()
        cls_list = [str(value) for key, value in all_obj.items()
                    if model in key]
        return len(cls_list)

    def _do_show(self, model: str, id: str) -> None:
        """Show details of an instance."""
        key = "{}.{}".format(model, id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def _do_destroy(self, model: str, id: str) -> None:
        """Destroy an instance."""
        key = "{}.{}".format(model, id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_create(self, arg: str) -> None:
        """Create a new instance of BaseModel and save it."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                model = self.classes_dict[arg]()
                model.save()
                print("{}".format(model.id))
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg: str) -> None:
        """Print the string representation of
        an instance based on the class.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id = args[1]
            model = self.classes_dict[args[0]]
            key = "{}.{}".format(model.__name__, id)
            try:
                model_instance = storage.all()[key]
                print(model_instance)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg: str) -> None:
        """Delete an instance based on the name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            model = args[0]
            id = args[1]
            model = self.classes_dict[model]
            key = "{}.{}".format(model.__name__, id)
            try:
                del storage.all()[key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line: str) -> None:
        """Print all string representations of
            instances based or not on the class.
        """
        all_obj = storage.all()
        if not line:
            cls_list = [str(value) for _, value in all_obj.items()]
            print(cls_list)
        else:
            cls_list = []
            if line in self.classes_dict:
                cls_list = [str(value) for key, value in all_obj.items()
                            if line in key]
                print(cls_list)
            else:
                print("** class doesn't exist **")

    def _do_update(self, key, kwargs):
        model = storage.all()[key]
        kwargs = ast.literal_eval(kwargs)
        for key, item in kwargs.items():
            setattr(model, key, item)
            model.save()

    def do_update(self, arg: str) -> None:
        """Update an instance based on the class
            name and id by adding or updating an attribute.
        """
        pattern = r'("[^"]+"|\S+)'
        comps = re.findall(pattern, arg)
        args = [comp.strip('"') for comp in comps]

        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id = args[1]
            model_class = self.classes_dict[args[0]]
            key = "{}.{}".format(model_class.__name__, id)

            try:
                if len(args) < 3:
                    print("** attribute name missing **")
                else:
                    attr = args[2]

                    if len(args) < 4:
                        print("** value missing **")
                    else:
                        model_instance = storage.all()[key]
                        if not model_instance:
                            print("** no instance found **")
                        else:
                            if hasattr(model_instance, attr):
                                attr_type = type(getattr(model_instance, attr))
                            else:
                                attr_type = (float if
                                             args[3].strip('""')
                                             .isdigit() else str)

                            casted_value = attr_type(args[3].strip('""'))
                            setattr(model_instance, attr, casted_value)
                            model_instance.save()

            except KeyError:
                print("** no instance found **")

    def do_EOF(self, line: str) -> bool:
        """Exit the console when encountering EOF."""
        return True

    def do_help(self, arg: str) -> bool | None:
        """Show available commands and usage."""
        return super().do_help(arg)

    def do_quit(self, arg: str) -> None:
        """Quit command to exit the program."""
        exit()


