"""Password hashing and security utilities"""

from passlib.context import CryptContext


class PasswordHasher:
    """Handles password hashing using bcrypt"""
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        """Creates password hash"""
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verifies if password matches hash"""
        return self.pwd_context.verify(plain_password, hashed_password)
