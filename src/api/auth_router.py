"""HTTP endpoints for authentication operations"""

from application.auth_service import AuthService, RegisterUserInput
from fastapi import APIRouter, Depends, HTTPException
from infrastructure.database import get_session
from infrastructure.security import PasswordHasher
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="", tags=["User Authentication"])

def get_auth_service(session: Session = Depends(get_session)):
    """Creates AuthService instance with dependencies"""

    return AuthService(session, PasswordHasher())

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
