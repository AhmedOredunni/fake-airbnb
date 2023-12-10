#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherit from the BaseModel class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""