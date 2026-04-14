# Import Session to interact with the database
from sqlalchemy.orm import Session

# Import User model (SQLAlchemy table)
from app.models.user import User

# Import Pydantic schema for user creation
from app.schemas.user import UserCreate

# Import security functions (hashing, verification, JWT creation)
from app.core.security import hash_password, verify_password, create_access_token


# Service class to handle authentication logic
class AuthService:


    # Static method → does not depend on class instance
    @staticmethod
    def register_user(db: Session, user_data: UserCreate):

        # 🔍 Check if user already exists with same email
        existing_user = db.query(User).filter(User.email == user_data.email).first()

        # If user exists → stop registration
        if existing_user:
            raise Exception("Email already registered")


        # Hash the plain password before storing
        hashed_pw = hash_password(user_data.password)


        # Create new User object (not yet saved to DB)
        new_user = User(
            email=user_data.email,        # Assign email
            hashed_password=hashed_pw     # Store hashed password (NOT plain)
        )


        # Add user to database session
        db.add(new_user)

        # Commit changes (actually saves to DB)
        db.commit()

        # Refresh instance (loads updated values like ID from DB)
        db.refresh(new_user)


        # Return created user object
        return new_user


    # Static method for login functionality
    @staticmethod
    def login_user(db: Session, email: str, password: str):

        # 🔍 Find user by email
        user = db.query(User).filter(User.email == email).first()

        # If user not found → invalid credentials
        if not user:
            raise Exception("Invalid email or password")


        # Verify password (plain vs hashed)
        if not verify_password(password, user.hashed_password):
            raise Exception("Invalid email or password")


        # Create JWT token (sub = subject = user id)
        token = create_access_token({
            "sub": str(user.id)
        })


        # Return token (used for authentication)
        return token