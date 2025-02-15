"""SQLAlchemy models for database persistence"""

from datetime import datetime

from sqlalchemy import (
    Boolean, 
    Column, 
    DateTime, 
    Integer,
    String
)

from .base import Base


class UserModel(Base):
    """Database model representing user data"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now())
