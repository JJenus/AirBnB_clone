#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class

    Attributes:
        name (str): name of amenity
    """

    name = ""
