#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review model

    Attributes:
        place_id (str): place id
        user_id (str): user id
        text (str): review text/comment
    """

    place_id = ""
    user = ""
    text = ""
