#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage():
    """Handle the file storage for the BaseModel class"""
    def __init__(self):
        """Called when the class is Initiated"""
        #string - path to the JSON file
        self.__file_path = "file.json"
        #dictionary - empty but will store all objects
        self.__objects = {}

    def all(self):
        """Return the dictionary object of the Model"""
        return self.__objects
    
    def new(self, obj):
        """Set a new object in the __objects dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        with open(self.__file_path, 'w') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                self.__objects = {}
                for key, value in obj_dict.items():
                    class_name, instance_id = key.split('.')
                    class_obj = globals().get(class_name)
                    if class_obj and issubclass(class_obj, BaseModel):
                        instance = class_obj(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            # Do nothing if the file doesn't exist
            pass

    