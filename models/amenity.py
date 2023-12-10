#!/usr/bin/python3
"""Amenity module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class to store amenity details"""
    def __init__(self, name=""):
        super().__init__()
        self.name = name

    def to_dict(self):
        amenity_dict = super().to_dict()
        amenity_dict["name"] = self.name
        return amenity_dict
