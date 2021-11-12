#!/usr/bin/python3
"""entry point for command interpreter"""
import cmd
import sys


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

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
