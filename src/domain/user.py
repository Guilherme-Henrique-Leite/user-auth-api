"""Domain models and business rules for user management"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    """Domain entity representing a user with business rules"""
    username: str
    email: str
    is_active: bool = True
    created_at: datetime = datetime.now()

    def validate_email(self) -> bool:
        """Validate email format"""
        return '@' in self.email
