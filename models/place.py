#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place model

    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): name of place
        description (str): description of place
        number_rooms (int): number of rooms in a place
        number_bathrooms (int): number of bathrooms in a place
        max_guest (int): maximum allowed quests
        price_by_night (int): price by night
        latitude (float): latitude of geolocation
        longitude (float): longitude of geolocation
        amenity_ids (list): `str`: amenity ids in that palce
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
    logitude = 0.0
    amenity_ids = []
