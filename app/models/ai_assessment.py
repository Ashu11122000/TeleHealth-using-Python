# Importing required components from SQLAlchemy (Python ORM for database interaction)
# Column → used to define a column in a database table
# Integer, String, DateTime → data types for columns (similar to SQL types like INT, VARCHAR, TIMESTAMP)
# ForeignKey → used to create relationships between tables (like referencing another table's primary key) 
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

# func → provides access to SQL functions (like NOW(), COUNT(), etc.)
from sqlalchemy.sql import func

# Base → the base class for all database models (created using declarative_base)
# It connects Python classes to database tables (ORM mapping)
from app.db.base import Base

# Defining a model (table) class
# AIAssessment → Python class representing a database table
class AIAssessment(Base):
    
    # __tablename__ → tells SQLAlchemy the name of the table in the database
    # Table name will be "ai_assessment"
    __tablename__ = "ai_assessment"
    
    # Primary key column (unique identifier for each row)
    # Column → defines a table column
    # Integer → data type (INT in SQL)
    # primary_key=True → makes this column the primary key (unique + not null)
    # index=True → creates an index for faster search queries
    id = Column(Integer, primary_key = True, index = True)
    
    # Foreign key column linking to users table
    # Integer → data type
    # ForeignKey("users.id") →
    #   means this column references the 'id' column of the 'users' table
    #   creates a relationship between AIAssessment and Users
    #   ensures referential integrity (no invalid user_id)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Column to store risk level (e.g., low, medium, high)
    # String → text data (VARCHAR in SQL)
    # nullable=False → this field is required (cannot be NULL)
    risk_level = Column(String, nullable = False)
    
    # Column to store AI-generated summary
    # String → text field
    # nullable=True by default → this field is optional
    summary = Column(String)
    
    # Timestamp column for record creation time
    # DateTime → stores date and time
    # timezone=True → stores timezone-aware timestamps
    # server_default=func.now() →
    #   default value is set by the database server (not Python)
    #   func.now() → SQL function (equivalent to NOW() in SQL)
    #   automatically sets current timestamp when record is created
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    