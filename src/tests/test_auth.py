"""Unit tests for authentication service"""

import pytest
from application.auth_service import AuthService, RegisterUserInput


@pytest.mark.asyncio
async def test_register_valid_user():
    """Tests successful user registration"""
    class MockRepository:
        async def get_by_email(self, email): return None
        async def create(self, user, password): return user

    class MockHasher:
        def hash_password(self, password): return "hashed"

    service = AuthService(MockRepository(), MockHasher())
    input_data = RegisterUserInput(
        username="test",
        email="test@test.com",
        password="password123"
    )

    success, error = await service.register(input_data)

    assert success
    assert error is None

@pytest.mark.asyncio
async def test_register_invalid_email():
    """Tests registration with invalid email"""
    service = AuthService(None, None)
    input_data = RegisterUserInput(
        username="test",
        email="invalid-email",
        password="password123"
    )

    success, error = await service.register(input_data)

    assert not success
    assert error == "Invalid email"
