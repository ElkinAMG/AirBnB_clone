#!/usr/bin/python3
"""Review Model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class Model that shows customer reviews"""
    place_id = ""
    user_id = ""
    text = ""
