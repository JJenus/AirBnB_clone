#!/usr/bin/python3
"""AirBnB console"""

import cmd
import re

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity


def parse(arg):
    """Make argument a readable list """
    return [com.strip() for com in arg.split()]


class HBNBCommand(cmd.Cmd):
    """AirBnB command line interpreter"""
    prompt = "(hbnb) "
    __classes = [
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def is_valid_command(self, command, action="create"):
        if len(command) < 1 and action != "all":
            print("** class name missing **")
            return False
        if command[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(command) < 2 and action not in ["create", "all"]:
            print("** instance id missing **")
            return False
        elif action not in ["create", "all"]:
            _id = f"{command[0]}.{command[1]}"
            if _id not in storage.all():
                print("** no instance found **")
                return False
            if len(command) < 3 and action == "update":
                print("** attribute name misssing **")
                return False
            if len(command) < 4 and action == "update":
                print("** value missing **")
                return False

        return True

    def default(self, line):
        args = line.split(".")
        if len(args) < 1:
            print("** invalid command **")
            return None

        _class = args[0]
        _action = args[1].split("(")[0]

        if _action == "all":
            self.do_all(_class)
        elif _action == "count" and self.is_valid_command(args, "all"):
            objs = [str(obj) for key, obj in storage.all().items()
                    if type(obj) is eval(args[0])]
            print(len(objs))
        elif _action == "show":
            _id = re.search('"(.*?)"', args[1]).group(1)
            self.do_show(f"{_class} {_id}")
        elif _action == "destroy":
            _id = re.search('"(.*?)"', args[1]).group(1)
            self.do_destroy(f"{_class} {_id}")
        elif _action == "update":
            arg_list = re.search("\((.*?)\)",
                    args[1]).group(1).split(",")
            if len(arg_list) > 2:
                raw_id = arg_list[0].replace('"', "").strip()
                attr = arg_list[1].replace('"', "").strip()
                val = arg_list[2].replace('"', "").strip()
                command = f"{_class} {raw_id} {attr} {val}"
            elif len(arg_list) > 1:
                raw_id = arg_list[0].replace('"', "").strip()
                _dict = eval(arg_list[1].strip())
                for attr, val in _dict.items():
                    command = f"{_class} {raw_id} {attr} {val}"
                    self.do_update(command)
                return None
            else:
                command = _class
            self.do_update(command)

    def do_create(self, arg):
        """Create creates and save a new instance"""

        args = parse(arg)
        if not self.is_valid_command(args, "create"):
            return None
        model = args[0]
        new_obj = eval(model)()
        storage.new(new_obj)
        storage.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on class name and id
        """

        args = parse(arg)
        if self.is_valid_command(args, "show"):
            _id = f"{args[0]}.{args[1]}"
            print(str(storage.all()[_id]))

    def do_destroy(self, arg):
        """Deletes an instance from storage"""

        args = parse(arg)
        if self.is_valid_command(args, "destroy"):
            _id = f"{args[0]}.{args[1]}"
            storage.all().pop(_id)
            storage.save()

    def do_all(self, arg):
        """Print all or print provided model instances"""

        args = parse(arg)
        if len(args) > 0 and self.is_valid_command(args, "all"):
            objs = [str(obj) for key, obj in storage.all().items()
                    if type(obj) is eval(args[0])]
        else:
            objs = [str(obj) for key, obj in storage.all().items()]
        print(objs)

    def do_update(self, arg):
        """Update a single attribute in object instance"""

        args = parse(arg)
        if not self.is_valid_command(args, "update"):
            return
        _id = f"{args[0]}.{args[1]}"
        attr = args[2]
        val = args[3]
        obj = storage.all()[_id].to_dict()
        obj[attr] = val
        model = obj["__class__"]
        obj.pop("__class__")
        n_obj = eval(model)(**obj)
        storage.new(n_obj)
        storage.save()

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
