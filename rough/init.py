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