"""
Create a DTO for register user
"""
from dataclasses import dataclass


@dataclass
class RegisterUserInput:
    """DTO for user registration data"""
    username: str
    email: str
    password: str
