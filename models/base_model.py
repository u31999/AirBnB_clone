#!/usr/bin/env python3
"""
This module define a base class for all common attributes/methods for other classes
"""
from datetime import datetime
import uuid
import models
time = "%Y-%m-%dT%H:%M:%S.%f"


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

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # Change modules tp __module here and in line 50
            self.__module__.storage.new(self)
            self.__module__.storage.save()

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        self.__module__.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
