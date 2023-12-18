#!/usr/bin/python3
"""The file storage engine"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place


class FileStorage:
    """The file storage module saves instances
    from the base model.
    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): store all objects by class id
    """

    cls_dict = {"BaseModel": BaseModel, "User": User,
                "State": State, "City": City,
                "Amenity": Amenity, "Place": Place, "Review": Review}

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
        serialized_objects = {key: obj.to_dict()
                              for key, obj in self.__objects.items()}
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
                    self.__objects = {
                        key: self.cls_dict[value["__class__"]](**value)
                        for key, value in serialized_objects.items()
                    }
        except FileNotFoundError:
            pass
