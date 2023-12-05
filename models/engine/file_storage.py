#!/usr/bin/python3
"""The file storage engine"""
import json
from models.base_model import BaseModel


class FileStorage:
    """The file storage module saves instances
        from the base model.
    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): store all objects by class id
    """

    def __init__(self):
        """Initialize FileStorage with default attributes"""
        self.__file_path = "files/store.json"
        self.__objects = {}

    def all(self):
        """Returns a dictionary of all 
            the objects in the storage
        """
        return self.__objects
    
    def delete(self, obj):
        """Removes an object from the dict"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        del self.__objects[key]
    
    def new(self, obj):
        """adds a new object to the __objects dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes the __objects attribute into a json string
            and save it in a json file
        """
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        json_str = json.dumps(serialized_objects)

        with open(self.__file_path, mode="w", encoding="UTF8") as f:
            f.write(json_str)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r", encoding="UTF8") as f:
                content = f.read()
                if content:
                    serialized_objects = json.loads(content)
                    self.__objects = {key: BaseModel(**value) for key, value in serialized_objects.items()}
        except FileNotFoundError:
            pass