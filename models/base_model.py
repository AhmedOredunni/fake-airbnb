#!/usr/bin/python3
import uuid
import datetime

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

    def save(self):
        # Update the public instance attribute updated_at with the current datetime
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        # Create a dictionary containing all keys/values of __dict__ of the instance
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
