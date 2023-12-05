#!/usr/bin/python3
"""The Base model for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """The base model has common attributes and
        methods for other classes

    Attributes:
        id (str): A unique identifier that is randomly generated using UUID.
        created_at (str): The timestamp when the instance was created.
        updated_at (str): The timestamp when the instance was last updated.

    Args:
        id (str): A unique id that is randomly
                  generated using UUID (default is None).
    """

    def __init__(self, id=None) -> None:
        """Initialize a new instance of the BaseModel class.

        Args:
            id (str): A unique id that is randomly
                      generated using UUID (default is None).
        """
        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id

        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) \
                {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now().isoformat

    def to_dict(self):
        """Returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__

        return self.__dict__
