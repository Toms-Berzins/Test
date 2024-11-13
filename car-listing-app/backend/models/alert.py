# Database model for alerts
from sqlalchemy import Column, Integer, ForeignKey, String
from .database import Base

class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    listing_id = Column(Integer, ForeignKey('listings.id'), nullable=False)
    message = Column(String, nullable=False)
    # ...existing code...