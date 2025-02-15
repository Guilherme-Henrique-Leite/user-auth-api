"""
Outsource routers
"""
from api.auth_router import auth_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(auth_router)
