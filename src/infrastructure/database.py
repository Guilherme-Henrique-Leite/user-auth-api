"""Database connection and session management"""

from contextlib import asynccontextmanager

from sqlalchemy.sql import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .base import Base
from .models import UserModel

engine = create_async_engine(
    "sqlite+aiosqlite:///./auth.db",
    echo=True
)

SessionLocal = async_sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

@asynccontextmanager
async def get_session():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

async def init_db():
    """Creates database tables"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

class UserRepository:
    """Handles database operations for User entity"""
    
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_email(self, email: str):
        result = await self.session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        return result.scalars().first()

    async def create(self, user, hashed_password: str):
        db_user = UserModel(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password
        )
        self.session.add(db_user)
        await self.session.commit()
        await self.session.refresh(db_user)
        return db_user
