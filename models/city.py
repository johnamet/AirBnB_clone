#!/usr/bin/python3
"""City module"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class to store city details"""
    def __init__(self, state_id="", name=""):
        super().__init__()
        self.state_id = state_id
        self.name = name

    def to_dict(self):
        city_dict = super().to_dict()
        city_dict["state_id"] = self.state_id
        city_dict["name"] = self.name
        return city_dict
