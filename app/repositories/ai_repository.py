# Importing Session from sqlalchemy.orm
# Session is the main interface used to interact with the database
# It allows us to add, update, delete, and query data
from sqlalchemy.orm import Session

# Importing AIAssessment model
# This represents a database table (likely storing AI analysis results)
from app.models.ai_assessment import AIAssessment

# Importing Symptom model
# This represents a database table for storing symptoms linked to an assessment
from app.models.symptom import Symptom

# Defining a repository class
# Repository pattern is used to separate database logic from business logic
class AIRepository:
    
    # @staticmethod means this method belongs to the class, not an instance
    # We can call it without creating an object of AIRepository
    @staticmethod
    def create_assessment(db: Session, user_id: int, risk_level: str, summary: str):
        
        # Creating a new AIAssessment object (row for database table)
        # This does NOT save to DB yet, just creates a Python object
        assessment = AIAssessment(
            user_id = user_id,    # Foreign key or reference to user
            risk_level = risk_level,    # AI-determined risk level
            summary = summary    # AI-generated summary
        )
        
        # Adding the object to the session
        # This marks it for insertion into the database
        db.add(assessment)
        
        # Committing the transaction
        # This actually writes the data into the database permanently
        db.commit()
        
        # Refreshing the object from the database
        # This loads updated values (like auto-generated ID)
        db.refresh(assessment)
        
        # Returning the saved assessment object
        return assessment
    
# Static method to add multiple symptoms linked to an assessment
    @staticmethod
    def add_symptoms(db: Session, assessment_id: int, symptoms: list):
        
        # Looping through each symptom in the input list
        # 'symptoms' is expected to be a list of objects (likely Pydantic models)
        for s in symptoms:
            
            # Creating a new Symptom object (row in symptoms table)
            symptom = Symptom(
                assessment_id = assessment_id,  # Foreign key linking to AIAssessment
                name = s.name,                  # Symptom name (e.g., fever)
                severity = s.severity           # Severity level
            )
            
            # Adding each symptom to the session
            # It will be saved when commit is called
            db.add(symptom)
        
        # Commit after adding all symptoms
        # This saves all symptom records in one transaction
        db.commit()
        
