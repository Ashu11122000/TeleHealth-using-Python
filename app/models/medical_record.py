# Importing required SQLAlchemy components to define database table columns
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

# func is used to call SQL functions like NOW() from the database side
from sqlalchemy.sql import func

# relationship is used to define relationships between tables (ORM-level linking)
from sqlalchemy.orm import relationship

# Base is the parent class for all models (comes from project setup)
# It connects this class to SQLAlchemy ORM and database metadata
from app.db.base import Base

# Define a model (table) named MedicalRecord
# This class will be mapped to a database table
class MedicalRecord(Base):
    
    # __tablename__ = defines the actual name of the table in the database
    __tablename__ = "medical_records"
    
    # id column:
    # Integer -> data type (whole number)
    # primary_key = True -> uniquely identifies each row
    # index = True -> creates an index for faster searching
    id = Column(Integer, primary_key = True, index = True)
    
    # user_id column:
    # Integer -> stores numeric user ID
    # ForeignKey("users.id") -> links this column to id column of users table
    # This establishes a database-level relationship (constraint)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # title column:
    # String -> text data type
    # nullable = False -> this field is mandatory (cannot be empty)
    title = Column(String, nullable = False)
    
    # description column:
    # String -> stores text (details about the medical record)
    # nullable = False -> must have a value
    description = Column(String, nullable = False)
    
    # created_at column:
    # DateTime -> stores date and time
    # timezone = True -> ensures timezone-aware timestamps
    # server_default = func.now() -> automatically sets current timestamp from DB
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    
    # ORM relationship:
    # relationship("User") -> links this model to User model (Python-level)
    # Allows accessing related user like: medical_record.user
    # NOTE: "User" must be another SQLAlchemy model
    user = relationship("User")