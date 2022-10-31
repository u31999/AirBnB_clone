#!/usr/bin/python3
"""
This is the console base for the unit
"""
import cmd
from models.base_model import BaseModel
import models
import json
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """  Command prompt to access models data """
    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def do_EOF(self, argv):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_quit(self, argv):
        """When executed, exits the console."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
