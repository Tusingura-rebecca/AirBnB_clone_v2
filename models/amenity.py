#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage_target
from sqlalchemy import Column, String


class Amenity(BaseModel):
    if storage_target == 'db':
    name = ""
