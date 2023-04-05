#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models import storage_target
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    if storage_target == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("state_id"), nullable=False)
        places = relationship("Place", backref='cities')
    else:
        state_id = ""
        name = ""
