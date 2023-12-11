#!/usr/bin/python3
"""Amenity module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class to store amenity details
    Attributes:
        name (str): name of amenity (defaults to empty str)

    Args:
        name (str): name of amenity (defaults to empty str)
    """

    def __init__(self, name="", **kwargs):
        super().__init__(self)
        self.name = name

    def to_dict(self):
        return super().to_dict()
