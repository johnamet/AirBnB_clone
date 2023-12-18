#!/usr/bin/python3
"""Place module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class representing information about a rental place.

    Attributes:
        city_id (str): The city id (defaults to an empty string).
        user_id (str): The user id (defaults to an empty string).
        name (str): The name of the place (defaults to an empty string).
        description (str): Description of the place
                            (defaults to an empty string).
        number_of_rooms (int): The number of rooms (defaults to 0).
        number_of_bathrooms (int): The number of bathrooms
                                    (defaults to 0).
        max_guests (int): Maximum guests the place can accommodate
                            (defaults to 0).
        price_by_night (int): Price per night for the place (defaults to 0).
        latitude (float): Latitudinal position of the place
                            (defaults to 0.0).
        longitude (float): Longitudinal position of the place
                            (defaults to 0.0).
        amenity_ids (list of str): List of amenity ids
                                    (defaults to an empty list).

    Args:
        city_id (str): City id  (defaults to an empty string).
        user_id (str): User id (defaults to an empty string).
        name (str): Name of the place (defaults to an empty string).
        description (str): Description of the place
                        (defaults to an empty string).
        number_of_rooms (int): Number of rooms (defaults to 0).
        number_of_bathrooms (int): Number of bathrooms
                                    (defaults to 0).
        max_guests (int): Maximum guests (defaults to 0).
        price_by_night (int): Price per night
                                (defaults to 0).
        latitude (float): Latitudinal position (defaults to 0.0).
        longitude (float): Longitudinal position
                            (defaults to 0.0).
        amenity_ids (list of str): List of amenity ids
                                    (defaults to an empty list).
    """

    def __init__(self, city_id="", user_id="", name="",
                 description="", number_of_rooms=0, number_of_bathrooms=0,
                 max_guests=0, price_by_night=0, latitude=0.0,
                 longitude=0.0, amenity_ids=[], **kwargs):
        super().__init__(**kwargs)
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_of_rooms = number_of_bathrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guests = max_guests
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids

    def to_dict(self):
        """Converts the Place instance to a dictionary."""
        return super().to_dict()
