#!/usr/bin/python3
"""The module contains one class, `HBNBCommand`
   This is to manage the objects of AirBnB project
"""
from cmd import Cmd
from models.base_model import BaseModel
from models import storage
import re

class HBNBCommand(Cmd):
    """The console is to manage the
        objects of AirBnB clone project.
    """

    prompt = "(hbnb) "
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it.

        Usage: create <class name>
        Example: create BaseModel
        """
        # a dictionary of classes
        classes_dict = {"BaseModel": BaseModel}

        if not arg:
            print("** class name missing **")
        else:
            try:
                model = classes_dict[arg]()
                model.save()
                print("{}".format(model.id))
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
            instance based on the class.

        Usage: show <class name> <id>
        Example: show BaseModel 1234-5678
        """
        # a dictionary of classes
        classes_dict = {"BaseModel": BaseModel}

        args = arg.split(" ")

        if not arg:
            print("** class name missing **")
        elif args[0] not in classes_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id = args[1]
            model = classes_dict[args[0]]
            key = "{}.{}".format(model.__name__, id)
            try:
                model_instance = storage.all()[key]
                print(model_instance)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the name and id.

        Usage: destroy <class name> <id>
        Example: destroy BaseModel 1234-5678
        """
        classes_dict = {"BaseModel": BaseModel}

        args = arg.split(" ")

        if not arg:
            print("** class name missing **")
        elif args[0] not in classes_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
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

    def do_all(self, line):
        """Prints all string representations of all
            instances based or not on the class.

        Usage: all [class name]
        Example: all BaseModel
        """
        classes_dict = {"BaseModel": BaseModel}
        all_obj = storage.all()
        if not line:
            cls_list = [str(value) for _, value in all_obj.items()]
            print(cls_list)
        else:
            if line in classes_dict:
                cls_list = [str(value) if line in key else ''
                            for key, value in all_obj.items()]
                print(cls_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
            by adding or updating attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Example: update BaseModel 1234-5678 name "John Doe"
        """        
        # a dictionary of classes
        classes_dict = {"BaseModel": BaseModel}
        pattern = r'("[^"]+"|\S+)'
        comps = re.findall(pattern, arg)
        args = [comp.strip('"') for comp in comps]

        # Check if the class name is missing
        if not args:
            print("** class name missing **")
        # check whether the class exists
        elif args[0] not in classes_dict:
            print("** class doesn't exist **")
        # check whether the instance id is missing
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id = args[1]
            model_class = classes_dict[args[0]]
            if not model_class:
                print("** no instance found **")
            else:
                key = "{}.{}".format(model_class.__name__, id)

                try:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        else:
                            attr = args[2]

                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                # check whether the instance exits
                                model_instance = storage.all()[key]
                                if not model_instance:
                                     print("** no instance found **")
                                else:
                                     # Get the attribute type from the class
                                     attr_type = type(getattr(model_instance, attr, None))
                                     # Cast the value ti the attribute type
                                     casted_value = attr_type(args[3].strip('""'))
                                     # update the attribute in the model instance
                                     setattr(model_instance, attr, casted_value)
                                     # save the changes
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
