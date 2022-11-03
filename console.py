#!/usr/bin/python3
"""AirBnB console"""
import cmd
from models.base_model import BaseModel
from models import storage

def parse(arg):
    """Make argument a readable list """
    return arg.split()

class HBNBCommand(cmd.Cmd):
    """AirBnB command line interpreter"""
    prompt = "(hbnb) "
    __classes = ["BaseModel"]

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
