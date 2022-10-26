#!/usr/bin/env python3
"""
This module define a base class for all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    A Base class for all hbnb module

    Public instance attributes:
    id: BaseModel id
    created_at: The creation datetime 
    updated_at: The last update date time

    Public instance methods:
    save(self): updates the public instance attribute updated_at with the current datetime
    to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance
    """

    def __init__(self):
        """Initialize Public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Updates attribute updated_at with the current datetime"""
        self.created_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        r_dict = dict(self.__dict__)
        r_dict['__class__'] = self.__class__.__name__
        r_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        r_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return r_dict
