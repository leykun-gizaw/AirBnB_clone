#!/usr/bin/python3
"""This is the city file"""
from models.base_model import BaseModel


class City(BaseModel):
    """the city of the user"""
    state_id = ""
    name = ""
