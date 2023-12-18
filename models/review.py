#!/usr/bin/python3
"""The review model """
from models.base_model import BaseModel


class Review(BaseModel):
    """ The review data class
    Attributes:
        place_id (str): The place id (defaults to an empty string)
        user_id (str): The user id (defaults to an empty string)
        text (str): The text (defaults to an empty string)

    Args:
        place_id (str): The place id (defaults to an empty string)
        user_id (str): The user id (defaults to an empty string)
        text (str): The text (defaults to an empty string)
    """

    def __init__(self, place_id="", user_id="", text="", **kwargs):
        super().__init__(**kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text

    def to_dict(self):
        return super().to_dict()
