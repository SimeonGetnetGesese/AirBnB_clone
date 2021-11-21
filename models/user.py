#!/usr/bin/python3
"""The user class is defined"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class User is created which inherits from the BaseModel class
        Attributes:
            first_name(str): First name of the user.
            last_name(str): Last name of the user.
            email(str): Email of the user.
            password(str): Password of the user.
    """

    first_name = ""
    last_name = ""
    email = ""
    password = ""
