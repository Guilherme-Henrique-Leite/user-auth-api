"""Domain models and business rules for user management"""

from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    """Domain entity representing a user with business rules"""
    username: str
    email: str
    id: int = None
    is_active: bool = True
    created_at: datetime = datetime.now()

    def validate_email(self) -> bool:
        """Validate email format"""
        return '@' in self.email
