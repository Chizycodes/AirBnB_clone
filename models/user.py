#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel
# from models.base_model import Base


class User(BaseModel):
    """Represents a user for a MySQL database.

    Inherits from Base Model.
    Attributes:
        email (String): The User's email id.
        password (String): Password.
        first_name (String): First name.
        last_name (String): Last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
