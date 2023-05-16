#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel
# from models.base_model import Base


class City(BaseModel):
    """Represents a city for a MySQL database.

    Inherits from Base Model.
    Attributes:
        state_id (String): The City's state id.
        name (String): The name of the City.
    """
    state_id = ""
    name = ""
