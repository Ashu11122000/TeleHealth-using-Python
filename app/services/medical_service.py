# Importing MedicalRecord model (SQLAlchemy ORM model)
# This represents the "medical_records" table in the database
from app.models.medical_record import MedicalRecord

# Importing MedicalRepository
# Repository layer handles direct database operations (CRUD queries)
from app.repositories.medical_repository import MedicalRepository

# Service Layer class
# This acts as a bridge between API (routes) and database (repository)
# It contains business logic (rules like who can create/view records)
class MedicalService:
    
    # Constructor method (called when object is created)
    def __init__(self):
        
        # Creating an instance of Medical Repository
        # This will be used to interact with the database
        self.repo = MedicalRepository()
        
    # Method to create a medical record
    # db -> database session (SQLAlchemy session)
    # current_user -> logged-in user (from authentication system)
    # data -> request body (Pydantic schema: MedicalRecordCreate)
    def create_record(self, db, current_user, data):
        
        # Business Rule:
        # Only users with role "doctor" are allowed to create records
        if current_user.role != "doctor":
            
        # Raising an exception if unauthorized
        # This stops execution and returns error to API
            raise Exception("Only doctors can add medical records")
        
        # Creating a new MedicalRecord object (ORM instance)
        # This object is not yer saved in DB
        record = MedicalRecord(
            
            # Assigning values from request data
            user_id = data.user_id,
            title = data.title,
            description = data.description
        )
        
        # Calling repository method to save record into database
        # repo.create() will handle add(), commit(), refresh()
        return self.repo.create(db, record)
    
    # Method to fetch medical records for a user
    # db -> database session
    # current_user -> logged-in user
    # user_id -> ID of the patient whose records are requested
    def get_records(self, db, current_user, user_id):
        
        # Access Control Rule:
        # If the logged-in user is a patient and trying to access
        # someone else's records -> deny access
        if current_user.role == "patient" and current_user.id != user_id:
            
            # Raise Exception if unauthorized access attempt
            raise Exception("Access Denied")
        
        # If authorized:
        # Call repository methods to fetch records by user_id
        return self.repo.get_by_user(db, user_id)
    