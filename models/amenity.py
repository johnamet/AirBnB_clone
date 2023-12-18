#!/usr/bin/python3
"""Amenity module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ The Amenity data class
    Attributes:
        name (str): The name of the amenity
                    (defaults to an empty an empty string)

    Args:
        name (str): the name of the amenity
                    (defaults to an empty string)
        kwargs (dict): Keyworded arguments
    """

    def __init__(self, name="", **kwargs):
        super().__init__(self)
        self.name = name

    def to_dict(self):
        return super().to_dict()
