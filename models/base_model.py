#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel():
    """ A class BaseModel which other classes will inherit from
   
        Attributes:
            id: A unique id created whenever an instance is created
            created_at: A time_date that stores the time when an instance is created
            updated_at: A time_date that stores the time whenever an instance is updated
    """
    def __init__(self, *args, **kwargs):
        """
            Called whenever the class is called
        """
        if kwargs:
            del kwargs['__class__']
            self.__dict__.update(kwargs)
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            # Assign with a string representation of a UUID
            self.id = str(uuid.uuid4())

            # Assign with the current datetime when an instance is created
            # and it will be updated every time you change your object
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Call the new method on storage for a new instance
            models.storage.new(self)

    def save(self):
        """
        Update the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        #call the save method on storage.
        models.storage.save()



    def to_dict(self):
        """
        Create a dictionary containing all keys/values of __dict__ of the instance

        """
        obj_dict = self.__dict__.copy()

        # Add __class__ key with the class name of the object
        obj_dict['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at to string object in ISO format
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


if __name__ == "__main__":
    pass
