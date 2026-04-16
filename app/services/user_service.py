# Import Session class from SQLAlchemy ORM
# Session is used to interact with the database (executes queries, commit changes)
from sqlalchemy.orm import Session

# Import UserRepository (Data Access Layer)
# Repository pattern is used to separate database logic from business logic
from app.repositories.user_repository import UserRepository

# Import User Model (SQLAlchemy ORM model)
# This represents the "users" table in the database
from app.models.user import User

# Service Layer class
# This layer contains business logic (acts between API layer and repository layer)
class UserService:
    
    # Static method means this function belongs to the class, 
    # but does not require an instance (object) of the class to be called
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User:
        """
        db: SQLAlchemy Session *=(database connection object)
        user_id: integer ID of the user
        return: User object (ORM model instance)
        """
        
        # Calls repository method to fetch user from database
        # Delegates database logic to repository layer
        return UserRepository.get_user_by_id(db, user_id)
    
    # Static method for updating user data
    @staticmethod
    def update_user(db:Session, user: User, update_data: dict) -> User:
        """
        db: SQLAlchemy Session
        user: existing User ORM object fetched from DB
        update_data: dictionary containing fields to update
                        e.g. {"name": "Ashish", "email": "test@mail.com"}
        return: updated User object
        """
        
        # Loop through each key-value pair in update_data dictionary
        # .items() returns (key, value pairs)
        for key, value in update_data.items():
            
            # setattr() is a built-in Python function
            # It dynamically sets attribute of an object
            # Example: setattr(user, "name", "Ashish") -> user.name = "Ashish"
            setattr(user, key, value)
        
        # Commit the transaction
        # This saves all changes permanently to the database    
        db.commit()
        
        # Refresh the user object from the database
        # Ensures the object has latest values (Especially useful for auto-generated fields)
        db.refresh(user)
        
        # Returns the updated user object
        return user
    