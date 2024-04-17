#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from models.place import Place_amenity


class Amenity(BaseModel, Base):
    """ Represents anemity data set """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("place", secondary=place_amenity)
