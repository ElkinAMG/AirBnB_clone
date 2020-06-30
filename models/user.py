#!/usr/bin/python3
"""User Model"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class Model that shows User imformation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
