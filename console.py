#!/usr/bin/python3
"""AirBnB console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """AirBnB command line interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line\n"""
        pass

    def do_EOF(self, arg):
        """Exit on end of line with EOF\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
