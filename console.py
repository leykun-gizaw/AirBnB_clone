#!/usr/bin/python3
"""entry point for command interpreter"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command line class"""
    cmd.use_rawinput = False

    def __init__(self):
        """initialises what happens on execution"""
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit or EOF command exits the program\n"""
        sys.exit(1)

    def emptyline(self):
        pass

    def do_create(self, args):
        """Create command creates a new object"""
        if args is not None:
            args = BaseModel()
            args.save()
            print(args.id)
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
