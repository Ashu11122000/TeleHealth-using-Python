# Import SQLAlchemy session
from sqlalchemy.orm import Session

# Import User model (DB table)
from app.models.user import User

# Import schema for user creation
from app.schemas.user import UserCreate


# Create a repository class for User
class UserRepository:

    # Create a new user in database
    def create_user(self, db: Session, user_data: UserCreate, hashed_password: str):
        """
        This function creates a new user in the database.

        db: database session
        user_data: data from request (email, password)
        hashed_password: encrypted password
        """

        # Create User object (ORM model)
        db_user = User(
            email=user_data.email,
            hashed_password=hashed_password,
            role="patient"  # default role
        )

        # Add to DB
        db.add(db_user)

        # Commit changes
        db.commit()

        # Refresh to get updated data (like ID)
        db.refresh(db_user)

        # Return created user
        return db_user


    # Get user by email
    def get_user_by_email(self, db: Session, email: str):
        """
        Fetch user using email
        """

        return db.query(User).filter(User.email == email).first()


    # Get user by ID
    def get_user_by_id(self, db: Session, user_id: int):
        """
        Fetch user using ID
        """

        return db.query(User).filter(User.id == user_id).first()