# Import BaseModel for creating schemas and EmailStr for email validation
from pydantic import BaseModel, EmailStr


# Schema for user login request (used when user logs in)
class UserLogin(BaseModel):

    # Email field with built-in validation (must be a valid email)
    email: EmailStr

    # Password entered by the user (plain text)
    password: str


# Schema for token response (returned after successful login)
class TokenResponse(BaseModel):

    # JWT access token string
    access_token: str

    # Type of token (default is "bearer")
    # This is required by authentication standards (used in headers)
    token_type: str = "bearer"