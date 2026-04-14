# Import Depends → for dependency injection
# HTTPException → to return proper API errors
# status → for standard HTTP status codes (cleaner than hardcoding numbers)
from fastapi import Depends, HTTPException, status

# OAuth2PasswordBearer → extracts token from Authorization header
from fastapi.security import OAuth2PasswordBearer

# Import DB session type
from sqlalchemy.orm import Session

# Import DB dependency (creates DB session per request)
from app.db.session import get_db

# Import function to decode JWT token
from app.core.security import decode_access_token

# Import User model (database table)
from app.models.user import User


# OAuth2 scheme
# tokenUrl="/auth/login" → tells Swagger where login endpoint is
# Used to get token from: Authorization: Bearer <token>
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# Dependency to get current authenticated user
def get_current_user(
    
    # Extract token from request header
    token: str = Depends(oauth2_scheme),  
    
    # Inject DB session
    db: Session = Depends(get_db)          
):
    # Decode JWT token
    payload = decode_access_token(token)

    # If token is invalid or expired
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    # Extract user ID from token payload ("sub" = subject)
    user_id = payload.get("sub")

    # If token doesn't contain user ID
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )

    # Fetch user from database
    user = db.query(User).filter(User.id == int(user_id)).first()

    # If user not found in DB
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # ✅ Return authenticated user
    return user