"""HTTP endpoints for authentication operations"""

from fastapi import (
    APIRouter, 
    Depends, 
    HTTPException
)
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.security import PasswordHasher
from infrastructure.database import get_session, UserRepository
from application.auth_service import AuthService, RegisterUserInput

auth_router = APIRouter(prefix="", tags=["User Authentication"])

async def get_auth_service(session: AsyncSession = Depends(get_session)):
    """Creates AuthService instance with dependencies"""
    async with session as db_session:
        return AuthService(
            user_repository=UserRepository(db_session),
            password_hasher=PasswordHasher()
        )

@auth_router.post("/register")
async def register(
    input_data: RegisterUserInput,
    auth_service: AuthService = Depends(get_auth_service)
):
    """Handles user registration endpoint"""
    success, error = await auth_service.register(input_data)

    if not success:
        raise HTTPException(status_code=400, detail=error)

    return {"message": "User registered successfully"}
