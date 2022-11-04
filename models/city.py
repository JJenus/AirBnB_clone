#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class

    Attributes:
        state_id (str): unique id of state
        name (str): name of state
    """

    state_id = ""
    name = ""
