#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel
# from models.base_model import Base


class State(BaseModel):
    """Represents a state for a MySQL database.

    Inherits from Base Model.
    Attributes:
        name (String): The name of the State.
    """
    name = ""
