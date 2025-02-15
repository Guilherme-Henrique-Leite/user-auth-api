"""Authentication service and data transfer objects"""

from typing import Optional

from application import RegisterUserInput
from domain.user import User


class AuthService:
    """Handles user authentication operations"""
    def __init__(self, user_repository, password_hasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    async def register(self, input_data: RegisterUserInput) -> tuple[bool, Optional[str]]:
        """
        Registers a new user in the system
        
        Returns:
            tuple: (success_status, error_message if any)
        """
        user = User(username=input_data.username, email=input_data.email)

        if not user.validate_email():
            return False, "Invalid email"

        if await self.user_repository.get_by_email(input_data.email):
            return False, "Email already registered"

        hashed_password = self.password_hasher.hash_password(input_data.password)
        await self.user_repository.create(user, hashed_password)

        return True, None
