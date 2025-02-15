"""
Main entry point for the Authentication User API.
"""

from contextlib import asynccontextmanager

from api import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles database initialization during application startup."""
    await init_db()
    yield

app = FastAPI(
    debug=True,
    title="Authentication User API",
    summary="API for authentication user using JWT",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
