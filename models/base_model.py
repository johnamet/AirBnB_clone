#!/usr/bin/python3
"""The Base model for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize a new instance of the BaseModel class.

        Args:
            kwargs (dict): Dictionary of attribute names and
                           values. (default is None)
        """
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue  # Skip '__class__' attribute
                if key in ['created_at', 'updated_at']:
                    # Convert string to datetime object
                    # based on the known format
                    setattr(self, key,
                            datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) \
                {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        from models import storage
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        self.__dict__["__class__"] = self.__class__.__name__

        # Check if created_at is a datetime object before calling isoformat
        if isinstance(self.created_at, datetime):
            self.__dict__["created_at"] = self.created_at.isoformat()

        # Check if updated_at is a datetime object before calling isoformat
        if isinstance(self.updated_at, datetime):
            self.__dict__["updated_at"] = self.updated_at.isoformat()

        return self.__dict__
