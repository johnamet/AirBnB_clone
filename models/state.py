#!/usr/bin/python3
"""State module"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class to store state details"""
    def __init__(self, name="", **kwargs):
        super().__init__(self)
        self.name = name

    def to_dict(self):
        state_dict = super().to_dict()
        state_dict["name"] = self.name
        return state_dict
