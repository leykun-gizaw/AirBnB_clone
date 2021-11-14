#!/usr/bin/python3
"""entry point for command interpreter"""
import cmd
import sys
from models import storage
from shlex import split
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

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
        """Overrides the builtin `emptyline`"""
        pass

    def do_create(self, args):
        """Create command creates a new object"""
        if args[0]:
            if args == "BaseModel":
                args = BaseModel()
                args.save()
                print(args.id)
            elif args != "BaseModel":
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")
            return

    def do_show(self, args):
        """displays the Object name and Id"""
        if args is None:
            print("** class name missing **")
        else:
            args.split()
            args[0] = BaseModel()
            my_path = models.engine.file_storage.FileStorage.classes
            if args[1] not in my_path.keys():
                print("** class doesn't exist **")
            else:
                print(args.__str__())

    def do_destroy(self, args):
        """deletes the instance, provided name and Id"""
        dele = args.split()
        arguments = "{}.{}".format(dele[0], dele[1])
        if len(dele) == 0:
            print("** class name missing **")
            return
        if len(dele) == 1:
            print("** instance id missing **")
            return
        if dele[0] not in FileStorage.classes.keys():
            print("** class doesn't exist **")
            return
        if arguments not in models.storage.all().keys():
            print("** no instance found **")
            return
        del models.storage.all()[arguments]
        models.storage.save

    def do_all(self, args):
        """all prints the string representation of all instances"""
        args.split()
        if len(args) and args[0] not in FileStorage.classes.keys():
            print("** class doesn't exist **")
        elif args is None or args[0] in FileStorage.classes.keys():
            objects = []
            for obj in storage.all().values():
                if len(args) and args[0] == obj.__class__.__name__:
                    objects.append(obj.__str__())
                elif len(args) == 0:
                    objects.append(obj.__str__())
                print(arg.__str__())

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
