# Import BaseModel (used to create schemas) and EmailStr (validates email format)
from pydantic import BaseModel, EmailStr


# Schema for creating a new user (used in request body)
class UserCreate(BaseModel):

    # Email field with built-in validation (must be a valid email format)
    email: EmailStr

    # Password field (plain password from user input)
    password: str


# Schema for sending user data in API responses
class UserResponse(BaseModel):

    # User ID (comes from database)
    id: int

    # Email (validated as proper email format)
    email: EmailStr

    # Role of user (patient / doctor / admin)
    role: str

    # Pydantic configuration class
    class Config:

        # Allows conversion from ORM model (SQLAlchemy object → Pydantic schema)
        from_attributes = True