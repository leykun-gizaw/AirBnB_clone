#!/usr/bin/python3
"""Module Defines `HBNBCommand` class"""
import cmd
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand subclass of cmd.Cmd."""

    classes_dict = {
        "User": User,
        "City": City,
        "Place": Place,
        "State": State,
        "Review": Review,
        "Amenity": Amenity,
        "BaseModel": BaseModel,
    }

    def __init__(self):
        """Object initializer.

        Args:
            self (object): <class '__main__.HBNBCommand'> type object

        Returns:
            None
        """
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "
        self.bm_object = None
        return None

    def do_create(self, line):
        """Create a new BaseModel instance.

        Args:
            self (object): <class '__main__.HBNBCommand'> type object
            line (str): argument string passed to interpreter

        Returns:
            None
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes_dict.keys():
            print("** class doesn't exist **")
        else:
            self.bm_object = HBNBCommand.classes_dict[line]()
            storage.save()
            print(self.bm_object.id)
        return None

    def do_show(self, line):
        """Show BaseModel type instance of given id.

        Args:
            self (object): <class '__main__.HBNBCommand'> type object
            line (str): argument string passed to interpreter

        Returns:
            None
        """
        if HBNBCommand.arg_count(line) == 2:
            if self.bm_object and self.bm_object.id == line.split()[1]:
                print(self.bm_object)
            else:
                key = line.split()[0] + '.' + line.split()[1]
                for k, v in storage.all().items():
                    if k == key:
                        print(v)
                        return None
                print("** no instance found **")
        return None

    def do_destroy(self, line):
        """Delete BaseModel type instance of given id.

        Args:
            self (object): <class '__main__.HBNBCommand'> type object
            line (str): argument string passed to interpreter

        Returns:
            None
        """
        if HBNBCommand.arg_count(line) == 2:
            key = line.split()[0] + '.' + line.split()[1]
            if key in list(storage.all().keys()):
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        return None

    def do_all(self, line):
        """Print a list of all BaseModel objects as string representation.

        Args:
            self (object): <class '__main__.HBNBCommand'> type object
            line (str): argument string passed to interpreter

        Returns:
            None
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes_dict.keys():
            print("** class doesn't exist **")
        else:
            bm_obj_list = []
            for *_, v in storage.all().items():
                if v.__class__.__name__ == line:
                    bm_obj_list.append(str(v))
            print(bm_obj_list)
        return None

    def do_update(self, line):
        """Update instance with given id with provided attribute.

        Args:
            self (object): <class '__main__.HBNBCommand'> type object
            line (str): argument string passed to interpreter

        Returns:
            None
        """
        argv = line.split(maxsplit=3)
        if HBNBCommand.arg_count(line, "do_update") == 4:
            key = argv[0] + '.' + argv[1]
            if key in list(storage.all().keys()):
                if argv[3][0] == '"' and argv[3][len(argv[3]) - 1] == '"':
                    setattr(storage.all()[key],argv[2], argv[3][1:-1])
                    storage.save()
            else:
                print("** no instance found **")
        return None

    def do_EOF(self, *_):
        """Terminate on EOF registration.

        <Ctrl+d> registered will cause this command handler method to execute.
        Return value of `True` will cause the interpreter to quit gracefully.

        Args:
            self (object): <class '__main__.HBNBCommand'> type object

        Returns:
            True
        """
        return True

    def do_quit(self, *_):
        """Exit interpreter when this command handler method is executed.

        Args:
            self (object): <class '__main__.HBNBCommand'> type object

        Returns:
            True
        """
        return True

    @staticmethod
    def arg_count(arg_str, handler=""):
        argv = arg_str.split(maxsplit=3)
        if not arg_str:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.classes_dict:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        elif len(argv) == 2:
            if handler == "do_update":
                print("** attribute name missing **")
            else:
                return 2
        elif len(argv) == 3 and handler == "do_update":
            print("** value missing **")
        elif len(argv) == 4:
            return 4
        return None

    def emptyline(self):
        pass
    pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
