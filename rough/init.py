if kwargs is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        # convert string to datetime object
                        setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
            # Add the missing updated_at attribute
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.datetime.now()
else:
    # Assign with a string representation of a UUID
    self.id = str(uuid.uuid4())

    # Assign with the current datetime when an instance is created
    # and it will be updated every time you change your object
    self.created_at = datetime.datetime.now()
    self.updated_at = datetime.datetime.now()



try:
    with open(self.__file_path, 'r') as file:
        obj_dict = json.load(file)
        # Assuming objects are created using the from_dict method
        self.__objects = {key: BaseModel.from_dict(value) for key, value in obj_dict.items()}
except FileNotFoundError:
    # Do nothing if the file doesn't exist
    pass


with open(self.__file_path, 'w') as file:
    obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
    json.dump(obj_dict, file)
    
#  obj_dict = json.load(file)
#                 self.__objects = {}
#                 for key, value in obj_dict.items():
#                     class_name, instance_id = key.split('.')
#                     class_obj = globals().get(class_name)
#                     if class_obj and issubclass(class_obj, BaseModel):
#                         instance = class_obj(**value)
#                         self.__objects[key] = instance
#         except FileNotFoundError:
#             # Do nothing if the file doesn't exist
#             pass

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