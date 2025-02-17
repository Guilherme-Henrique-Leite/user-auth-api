# User Authentication API

A secure FastAPI service for user management with JWT authentication.

## Key Features
- User registration with password hashing
- Clean architecture structure
- Test-driven development
- Docker/DevContainer ready

## Tech Stack
- **Python 3.11**
- FastAPI
- SQLAlchemy + SQLite
- Pytest
- Bcrypt

## Usage
1. Start dev environment:
```
uv venv .venv && source .venv/bin/activate
uv pip install -e .
uvicorn src.main:app --reload
```

2. Access docs at `http://localhost:8000/docs`

## Testing
```
ruff check .
uv run pytest
```
