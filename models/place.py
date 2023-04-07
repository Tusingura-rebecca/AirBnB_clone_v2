#!/usr/bin/python3
""" Place module"""
from models.base_model import BaseModel, Base
from models import storage_target, storage
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


if storage_target == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey(
                                    "place_id",
                                    onupdate="CASCACE",
                                    ondelete="CASCADE"
                                    ),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey(
                                    "amenity_id",
                                    onupdate="CASCACE",
                                    ondelete="CASCADE"),
                                 primary_key=True, nullable=False))


class Place(BaseModel):
    """ A place to stay """
    if storage_target == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey="cities.id", nullable=False)
        user_id = Column(String(60), ForeignKey="cities.id", nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref='place')
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 backref="place_amenities",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    if storage_target != "db":
        @property
        def reviews(self):
            """getter, returns list of review instances related to the place"""
            from models.review import Review
            review_list = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter, returns Amenity instances list related to the place"""
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(Amenity):
            """setter, adds amenity.id to amenity_ids"""
            Amenity.amenity_ids.append(Amenity.id)
