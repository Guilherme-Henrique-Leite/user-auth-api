"""SQLAlchemy models for database persistence"""

from datetime import datetime

from sqlalchemy import (
    Boolean, 
    Column, 
    DateTime, 
    String
)

from .database import Base


class UserModel(Base):
    """Database model representing user data"""
    __tablename__ = "users"

    username = Column(String, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
