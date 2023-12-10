#!/usr/bin/python3
"""Place module"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class to store place details"""
    def __init__(self, city_id="", user_id="", name="", description="",
                 number_rooms=0, number_bathrooms=0, max_guest=0,
                 price_by_night=0, latitude=0.0, longitude=0.0,
                 amenity_ids=[]):
        super().__init__()
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids

    def to_dict(self):
        place_dict = super().to_dict()
        place_dict.update({
            "city_id": self.city_id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "number_rooms": self.number_rooms,
            "number_bathrooms": self.number_bathrooms,
            "max_guest": self.max_guest,
            "price_by_night": self.price_by_night,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "amenity_ids": self.amenity_ids,
        })
        return place_dict
