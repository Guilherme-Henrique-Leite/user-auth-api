"""Database connection and session management"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine(
    "sqlite:///./auth.db",
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    """Provides database session with automatic cleanup"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def init_db():
    """Creates database tables"""
    Base.metadata.create_all(bind=engine)
