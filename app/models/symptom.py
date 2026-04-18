# Importing required components from SQLAlchemy ORM
# Column → used to define a column in a database table
# Integer, String → data types (like INT, VARCHAR in SQL)
# ForeignKey → used to create a relationship between two tables
from sqlalchemy import Column, Integer, String, ForeignKey  

# Base → parent class for all models (created using declarative_base)
# It tells SQLAlchemy that this class should be mapped to a database table
from app.db.base import Base  


# Defining the Symptom model (represents a table in the database)
# Symptom → Python class that maps to a database table

class Symptom(Base):
    # __tablename__ → name of the table in the database
    # Table will be created as "symptoms"
    __tablename__ = "symptoms"
    

    # Primary key column (unique identifier for each symptom)
    # Integer → numeric data type
    # primary_key=True → makes this column unique and not null
    # index=True → creates an index to improve query performance
    id = Column(Integer, primary_key=True, index=True)


    # Foreign key column linking to AI assessment table
    # ForeignKey("ai_assessments.id") →
    #   links this column to the 'id' column of 'ai_assessments' table
    #   creates a relationship (many symptoms → one assessment)
    #   ensures data consistency (no invalid assessment_id allowed)
    assessment_id = Column(Integer, ForeignKey("ai_assessments.id"))

    # Column to store symptom name (e.g., fever, cough)
    # String → text data (VARCHAR)
    # nullable=False → this field is required (cannot be empty)
    name = Column(String, nullable=False)

    # Column to store severity level of symptom
    # String → text field
    # nullable=True by default → optional field
    # Example values: "low", "medium", "high"
    severity = Column(String)  # low / medium / high
    