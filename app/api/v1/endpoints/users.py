# Import APIRouter -> used to create modular route groups in FastAPI
# Depends -> for dependency injection (auth, db, etc.)
# HTTPException -> to return structured API errors
# status -> standard HTTP status codes (400, 401, 404, etc.)
from fastapi import APIRouter, Depends, HTTPException, status

# Import SQLAlchemy session -> used for DB operations
from sqlalchemy.orm import Session

# Import authentication dependencies
# get_current_active_user -> ensures user is logged in + active
# required_role -> restricts access based on role (RBAC)
from app.api.deps import (
    get_current_active_user,
    require_role
)

# Import DB Dependency
# get_db -> provides database session automatically
from app.db.session import get_db

# Import User ORM model (represents users table)
from app.models.user import User

# Import Service layer
# Contains business logic
from app.services.user_service import UserService

# Create router instance
# This helps organize endpoints (e.g., /users, /auth, etc.)
router = APIRouter()

# 1. GET CURRENT USER PROFILE
@router.get("/me")
def get_my_profile(
    
    # Inject authenticated and active user
    current_user: User = Depends(get_current_active_user)
):
    """
    Get logged-in user's profile.
    """
    
    # Simply return current user object
    # FastAPI automatically converts ORM -> JSON (via Pydantic if configured)
    return current_user

# 2. UPDATE USER PROFILE
@router.put("/update")
def update_profile(
    
    # Request body (raw dictionary)
    # Contains fields to update
    update_data: dict,
    
    # Inject DB session
    db: Session = Depends(get_db),
    
    # Inject authenticated user
    current_user: User = Depends(get_current_active_user)
):
    """
    Update logged-in user's profile.
    """

    # Prevent updating sensitive fields (security measures)
    # These fields should not be editable by user
    restricted_fields = ["id", "hashed_password", "role"]
    
    # Loop through restricted fields
    for field in restricted_fields:
        
        # If user tries to update restricted field
        if field in update_data:
            raise HTTPException(
                
                # 400 -> Bad request
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"You cannot update '{field}'"
            )
            
    # Call service layer to update user
    updated_user = UserService.update_user(
        db=db,
        user=current_user,
        update_data=update_data
    )
    
    # Return updated user
    return updated_user

# 3. ADMIN ONLY — GET ALL USERS
@router.get("/all")
def get_all_users(
    
    # Inject DB session
    db: Session = Depends(get_db),
    
    # RBAC: only allow admin role
    # require_role(["admin"]) returns a dependency function
    current_user: User = Depends(require_role(["admin"]))
):
    """
    Admin can view all users.
    """
    
    # Query ll users from database
    # SELECT * FROM users
    users = db.query(User).all()
    
    # Return list of users
    return users

# 4. ADMIN ONLY — GET USER BY ID
@router.get("/{user_id}")
def get_user_by_id(
    
    # Path parameter (from URL)
    user_id: int,
    
    # Inject DB session
    db: Session = Depends(get_db),
    
    # RBAC: only admin allowed
    current_user: User = Depends(require_role(["admin"]))
):
    """
    Admin can fetch any user by ID.
    """
    
    # Query user by ID
    # WHERE id = user_id
    user = db.query(User).filter(User.id == user_id).first()
    
    # If user does not exits
    if not user:
        raise HTTPException(
            
            # 404 -> Not Found
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user

# 5. ADMIN ONLY — DELETE USER
@router.delete("/{user_id}")
def delete_user(
    
    # Path parameter
    user_id: int,
    
    # Inject DB session
    db: Session = Depends(get_db),
    # RBAC: only admin allowed
    current_user: User = Depends(require_role(["admin"]))
):
    """
    Admin can delete users.
    """
    
    # Fetch user from DB
    user = db.query(User).filter(User.id == user_id).first()
    
    # If user not found
    if not user:
        raise HTTPException(
            # 404 -> Not Found
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Delete user object
    # Marks it for deletion
    db.delete(user)
    
    # Commit transaction -> permanently deletes from DB
    db.commit()
    
    # Return success message
    return {"message": "User deleted successfully"}