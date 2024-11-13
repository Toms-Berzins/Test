# Database model for listings
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Listing(Base):
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    # ...existing code...