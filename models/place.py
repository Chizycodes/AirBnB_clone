#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel
# from models.base_model import Base


class Place(BaseModel):
    """Represents a place for a MySQL database.

    Inherits from Base Model.
    Attributes:
        city_id (String): The place's city id.
        user_id (String): The place's user id.
        name ( String): The name.
        description ( String): The description.
        number_rooms ( Integer): The number of rooms.
        number_bathrooms ( Integer): The number of bathrooms.
        max_guest ( Integer): The maximum number of guests.
        price_by_night ( Integer): The price by night.
        latitude ( Float): The place's latitude.
        longitude ( Float): The place's longitude.
        amenities ( relationship): The Place-Amenity relationship.
        amenity_ids (list): An id list of all linked amenities.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
