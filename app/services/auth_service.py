# Import DB session
from sqlalchemy.orm import Session

# Import schemas
from app.schemas.user import UserCreate
from app.schemas.auth import UserLogin

# Import security functions
from app.core.security import hash_password, verify_password, create_access_token

# Import repository
from app.repositories.user_repository import UserRepository


# Create instance of repository
user_repo = UserRepository()


class AuthService:

    # Register user
    def register_user(self, db: Session, user_data: UserCreate):

        # Check if user already exists
        existing_user = user_repo.get_user_by_email(db, user_data.email)

        if existing_user:
            raise Exception("User already exists")

        # Hash password
        hashed_password = hash_password(user_data.password)

        # Create user using repository
        new_user = user_repo.create_user(db, user_data, hashed_password)

        return new_user


    # Login user
    def login_user(self, db: Session, user_data: UserLogin):

        # Get user from DB
        user = user_repo.get_user_by_email(db, user_data.email)

        if not user:
            raise Exception("Invalid credentials")

        # Verify password
        if not verify_password(user_data.password, user.hashed_password):
            raise Exception("Invalid credentials")

        # Generate JWT token
        token = create_access_token(data={"sub": str(user.id)})

        return {
            "access_token": token,
            "token_type": "bearer"
        }