"""
Create a DTO for register user
"""
from pydantic import BaseModel


class RegisterUserInput(BaseModel):
    """DTO for user registration data"""
    username: str
    email: str
    password: str
