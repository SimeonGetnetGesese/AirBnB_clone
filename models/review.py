#!/usr/bin/python3
"""Review class is defined"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class is created which inherits from BaseModel
        Attributes:
            place_id(str): Place id of the user.
            user_id(str): User id of the user.
            text(str): text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
