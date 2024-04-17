#!/usr/bin/python3
"""This is the amenity class"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    @staticmethod
    def get_place_amenities():
        from models.place import Place  # Lazy import inside a method
        if getenv("HBNB_TYPE_STORAGE") == "db":
            return relationship('Place',
                                secondary='place_amenity',
                                back_populates='amenities')
        else:
            return None

