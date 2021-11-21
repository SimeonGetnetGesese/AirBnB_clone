#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """A place class is created, and inherits from Basemodel class.
        Attributes:
            name(str): Name of the place.
            city_id(str): Id of the city.
            user_id(str): Id of the User.
            description(str): place description.
            number_rooms(int): Number of rooms.
            number_bathrooms (int): Number of bathrooms.
            max_guest (int): Maximum number of guests.
            price_by_night (int): Price for a night.
            latitude (float): Latitude of the place.
            longitude (float): Longitude of the place.
            amenity_ids (list): List of Amenity ids.
    """

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
