#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel
# from models.base_model import Base


class Review(BaseModel):
    """Represents a state for a MySQL database.

    Inherits from Base Model.
    Attributes:
        place_id (String): The Review's place id.
        name (String): The name of the State.
    """
    place_id = ""
    user_id = ""
    text = ""
