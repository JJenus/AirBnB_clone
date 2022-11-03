#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage

"""AirBnB_clone base module"""


class BaseModel:
    """ BaseModel
    """

    def __init__(self, *args, **kwargs):
        """First instance of the base class

        Args:
            *args (tuple): tuple of instance attributes
            **kwargs (dict): dictionary of instance attributes
        """

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        String representation of BaseModel
        """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Keeps track of updated time
        updates updated_at to current time
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of an instance."""
        this_dict = self.__dict__.copy()
        this_dict["__class__"] = type(self).__name__
        this_dict["created_at"] = self.created_at.isoformat()
        this_dict["updated_at"] = self.updated_at.isoformat()
        return this_dict
