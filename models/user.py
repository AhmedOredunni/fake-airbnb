#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """A user class that inherit from the Basemodel Class"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        
        
    def to_dict(self):
        """Return a dictionary representation of the User instance"""
        user_dict = super().to_dict()
        user_dict.update({
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        return user_dict
        
    