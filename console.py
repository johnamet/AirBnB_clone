#!/usr/bin/python3
"""The module contains one class, `Console`
    This is to manage the objects of AirBnB project
"""
from cmd import Cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(Cmd):
    """The console is to manage the
        objects of AirBnB clone project.
    """

    prompt = "(hbnb) "
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it."""

        # a dictionary of classes
        classes_dict = {"BaseModel": BaseModel}

        if arg is None or len(arg) == 0:
                    print("** class name missing **")
        else:     
            try:
                model = classes_dict[arg]()
                model.save()
                print("{}".format(model.id))
            except KeyError:
                print("**class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
            instance based on the class."""
        
        # a dictionary of classes
        classes_dict = {"BaseModel": BaseModel}

        args = arg.split(" ")

        if len(arg) == 0 or arg is None:
            print("** class name missing **")
        elif args[0] not in classes_dict.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            model = args[0]
            id = args[1]
            model = classes_dict[model]
            key = "{}.{}".format(model.__name__, id)
            try:
                    model = storage.all()[key]
                    print(model)
            except KeyError:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance base on the name and id"""
        classes_dict = {"BaseModel": BaseModel}

        args = arg.split(" ")

        if len(arg) == 0 or arg is None:
            print("** class name missing **")
        elif args[0] not in classes_dict.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            model = args[0]
            id = args[1]
            model = classes_dict[model]
            key = "{}.{}".format(model.__name__, id)
            try:
                    del storage.all()[key]
                    storage.save()
            except KeyError:
                    print("** no instance found **")

        
    def do_EOF(self, line):
        """Exit the console when encountering EOF."""
        return True
    
    def do_help(self, arg: str) -> bool | None:
        """Shows available commands and usage.

        Args:
            arg (str): The argument to get help for.

        Returns:
            bool or None: The result of the help command execution.
        """
        return super().do_help(arg)
    
    def do_quit(self, arg):
        """Quit command to exit the program
        """
        exit()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
