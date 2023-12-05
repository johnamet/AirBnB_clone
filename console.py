#!/usr/bin/python3
"""The module contains one class, `Console`
    This is to manage the objects of AirBnB project
"""
from cmd import Cmd


class Console(Cmd):
    """The console is to manage the
        objects of AirBnB clone project.
    """

    intro = "AirBnB clone Management Console.   \
        Type help or ? to list commands.\n"
    prompt = "(hbnb) "

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
        """Exit the console.

        Args:
            arg: Argument (unused in this implementation).
        """
        exit()


if __name__ == "__main__":
    Console().cmdloop()