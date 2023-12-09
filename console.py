#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """Handle the commandline integration of the website"""
    base_model = BaseModel()
    prompt = "(hbnb) "
    
    def do_create(self, line):
        """Create and instance of the class Passed"""
        if not line:
            print("** class name missing **")
        elif line != type(self.base_model).__name__:
            print("** class doesn't exist **")
        else:
            self.base_model.save()
            print(self.base_model.id)
            
    def do_show(self, line):
        """Showed the String representation of the instance with a given id. """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] != type(self.base_model).__name__:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            obj = models.storage.all().get(obj_key)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)
        
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] != type(self.base_model).__name__:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            objects = models.storage.all()
            obj = objects.get(obj_key)
            if not obj:
                print("** no instance found **")
            else:
                del objects[obj_key]
                models.storage.save()

    def do_all(self, line):
        """Prints all string representations of instances based on the class name."""
        args = line.split()
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] != type(self.base_model).__name__:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            print([str(obj) for key, obj in objects.items() if key.startswith(class_name)])
            
    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] != type(self.base_model).__name__:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            objects = models.storage.all()
            obj = objects.get(obj_key)
            if not obj:
                print("** no instance found **")
            else:
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, eval(attr_value))
                models.storage.save()
        
    
    def do_EOF(self, line):
        """Use to exit the program"""
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()