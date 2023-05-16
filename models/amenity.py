#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel
# from models.base_model import Base


class Amenity(BaseModel):
    """Represents a amenity for a MySQL database.

    Inherits from Base Model.
    Attributes:
        name (String): The name of the Amenity.
    """
    name = ""
