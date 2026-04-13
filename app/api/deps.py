# SessionLocal: Factory that creates a new database session (connection handler)
# type: ignore -> Tells type-checkers (like mypy) to ignore type-related warnings for this import
from app.db.session import SessionLocal # type: ignore

# Generator: A type hint when a function yields values instead of returning once
# In FastAPI, dependencies that use `yield` are treated as context-managed resources
from typing import Generator

# get_db: Dependency function used in FastAPI to provide a DB session per request
def get_db() -> Generator:
    
    # Create a new database session (a connection to interact with DB)
    db = SessionLocal()
    
    try:
        # yield: Pauses the function that returns the DB session to the route
        # FastAPI uses this to inject the session into API endpoints
        yield db
    finally:
        # close(): Closes the database session after request is completed
        # Prevents connection leaks and free resources
        db.close()