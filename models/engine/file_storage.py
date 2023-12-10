#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:
    """Handle the file storage for the BaseModel class"""
    #string - path to the JSON file
    __file_path = "file.json"
    #dictionary - empty but will store all objects
    __objects = {}

    def all(self):
        """Return the dictionary object of the Model"""
        return self.__objects
    
    def new(self, obj):
        """Set a new object in the __objects dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
               data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                # class_name = class_name.capitalize()
                if class_name == 'State':
                    obj = State(**value)
                elif class_name == 'City':
                    value['state'] = self.__objects["State.{}".format(value['state_id'])]
                    obj = City(**value)
                elif class_name == 'Amenity':
                    obj = Amenity(**value)
                elif class_name == 'Place':
                    value['user'] = self.__objects["User.{}".format(value['user_id'])]
                    value['city'] = self.__objects["City.{}".format(value['city_id'])]
                    obj = Place(**value)
                elif class_name == 'Review':
                    value['user'] = self.__objects["User.{}".format(value['user_id'])]
                    value['place'] = self.__objects["Place.{}".format(value['place_id'])]
                    obj = Review(**value)
                elif class_name == 'User':
                    obj = User(**value)
                else:
                    obj = BaseModel(**value)
                # if class_name == 'User':
                #     obj = User(**obj_dict)
                # else:
                #     obj = BaseModel(**obj_dict)

                self.__objects[key] = obj

        except FileNotFoundError:
            pass

    