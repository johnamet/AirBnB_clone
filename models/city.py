#!/usr/bin/python3
"""A user class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """User class to store users detail
    Attributes:
        state_id (str): The state is  (defaults to empty string)
        name (str): The name of the city

    Args:
        state_id (str): The state is (defaults to empty string)
        name (str): The name of the city
        """

    def __init__(self, state_id="", name="", **kwargs):
        super().__init__(self)
        self.state_id = state_id
        self.name = name

    def to_dict(self):
        return super().to_dict()
