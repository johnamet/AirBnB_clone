#!/usr/bin/python3
"""The city module contains onlyone class `City`
    which inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """The City class inherits from the BaseModel
    Attributes:
        state_id (str): The state id
        name (str): The name of the city

    Args:
        state_id (str): The state id
        name (str): The name of the city
    """

    def __init__(self, state_id=None, name=None, **kwargs):
        super().__init__(self)
        self.state_id = state_id
        self.name = name

    def to_dict(self):
        return super().to_dict()
