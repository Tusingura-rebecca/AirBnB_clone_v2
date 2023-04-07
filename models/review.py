#!/usr/bin/python3
""" Review module"""
from models.base_model import BaseModel
from models import storage_target
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """ Review classto store review information """
    if storage_target == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey="places.id", nullable=False)
        user_id = Column(String(60), ForeignKey="user.id", nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
