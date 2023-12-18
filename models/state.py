#!/usr/bin/python3
"""The place model that inherits the BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """The state class inherits from the BaseModel
    Attributes:
        name (str): The name of the state

    Args"
        name (str): The name of the state
    """

    def __init__(self, name="", **kwargs):
        super().__init__(self)
        self.name = name

    def to_dict(self):
        return super().to_dict()
