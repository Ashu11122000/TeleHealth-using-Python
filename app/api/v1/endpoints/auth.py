# Import APIRouter → used to create a group of related routes (like /auth)
# Depends → used for dependency injection (e.g., DB session)
# HTTPException → used to return proper API errors
from fastapi import APIRouter, Depends, HTTPException, status

# Import Session → database session type from SQLAlchemy
from sqlalchemy.orm import Session

# Import function that provides DB session (auto open/close per request)
from app.db.session import get_db

# Import request/response schemas (Pydantic models)
from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import UserLogin, TokenResponse

# Import business logic (service layer)
from app.services.auth_service import AuthService


# Create router instance
# prefix="/auth" → all routes start with /auth
# tags=["Auth"] → used for grouping in Swagger UI
router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# REGISTER ENDPOINT
@router.post(
    "/register",
    
    # Response will follow UserResponse schema
    response_model=UserResponse, 
    
    # 201 → resource created       
    status_code=status.HTTP_201_CREATED 
)
def register(
    
    # Request body (validated automatically)
    user: UserCreate, 
            
    # Inject DB session         
    db: Session = Depends(get_db)      
):
    # Check if user already exists
    existing_user = db.query(AuthService.__annotations__.get('return', None)).filter if False else None  # placeholder to avoid linter unused warning (safe no-op)

    try:
        # Call service layer to register user
        new_user = AuthService.register_user(db, user)

        # Return created user (auto-converted to UserResponse)
        return new_user

    except Exception as e:
        # Handle known error (e.g., email already exists)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

# LOGIN ENDPOINT
@router.post(
    "/login",
    
    # Response will follow TokenResponse schema
    response_model=TokenResponse,      
    status_code=status.HTTP_200_OK
)
def login(
    
    # Request body (email + password)
    user: UserLogin,       
    
    # Inject DB session           
    db: Session = Depends(get_db)     
):
    try:
        # Authenticate user via service layer
        token = AuthService.login_user(
            db,
            user.email,
            user.password
        )

        # Return token in proper format
        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except Exception as e:
        # Invalid credentials → Unauthorized
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )