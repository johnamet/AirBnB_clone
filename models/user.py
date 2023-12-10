#!/usr/bin/python3
"""A user class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class to store users detail
    Attributes:
        email (str): The email of the user
        password (str): The password of the user
        first_name (str): The first_name of the user
        last_name (str): The last_name of the user
        id (str): a uuid it inherits from the base class

    Args:
        email (str): the email of the user
        password (str): the password of the user
        first_name (str): the first name of the user
        last_name (str): the last name of the user
        """

    def __init__(self, email=None, password=None,
                 first_name=None, last_name=None, **kwargs):
        super().__init__(self)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        super().to_dict()
