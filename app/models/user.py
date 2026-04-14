# Importing required SQLAlchemy column types
from sqlalchemy import Column, Integer, String, Boolean, DateTime

# Importing datetime to automatically store current timestamp
from datetime import datetime

# Import Base class (this is the base class for all database models)
# It connects this model to SQLAlchemy ORM
from app.db.base import Base

# Defining a User model (table) that inherits from Base
class User(Base):
    
    # Name of the table in the database
    __tablename__ = "users"
    
    # id column (uniquely identifier for each user)
    # Data type: user
    # Marks this column as primary key
    # Creates an index for faster lookup
    id = Column(Integer, primary_key = True, index = True)
    
    # Email column
    # Data type: String (text)
    # Ensures no duplicate emails
    # Adds index for faster search
    # Cannot be NULL (must have a value)
    email = Column(String, unique = True, index = True, nullable = False)
    
    # Hashed password column (we store hashed password, not plain text)
    # Data Type: String
    # Must always have a value (cannot be NULL)
    hashed_password = Column(String, nullable = False)
    
    # Role Column (defines types of user like patient, doctor or admin)
    # Data type: String (text)
    # Default value if not provided
    role = Column(String, default = "patient")
    
    # Boolean column to check if user is active or not
    # Data type: True/False
    # Default value is True (means active user)
    is_active = Column(Boolean, default = True)
    
    # Timestamp column to store when the user was created
    # Data type: Date and Time
    # Automatically stores current UTC time
    created_at = Column(DateTime, default = datetime.utcnow)
    
    