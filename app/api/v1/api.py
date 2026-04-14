# Import APIRouter → used to combine multiple route groups
from fastapi import APIRouter

# Import auth routes (the router we created in auth.py)
from app.api.v1.endpoints import auth


# Create main API router
# This acts as a central place to include all endpoint modules
api_router = APIRouter()


# Include auth routes into main router
# Now all routes from auth.router will be available
# Example:
# /auth/register
# /auth/login
api_router.include_router(auth.router)