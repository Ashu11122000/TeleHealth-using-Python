# Importing APIRouter -> used to create modular route groups
# Depends -> used for dependency injection (very important in FastAPI)
from fastapi import APIRouter, Depends

# Import Session -> SQLAlchemy database session
# Used to interact with the database (queries, inserts, etc.)
from sqlalchemy.orm import Session

# Import dependency functions:
# get_db -> provides database session
# get_current_user -> returns currently logged-in user
from app.api.deps import get_db, get_current_user

# Importing Pydantic schema for request validation
from app.schemas.medical_record import MedicalRecordCreate

# Importing service layer (business logic)
from app.services.medical_service import MedicalService

# Creating a router object
# This helps routes instead of putting everything in main.py
router = APIRouter()

# Creating instance of service layer
service = MedicalService()

# POST API -> Add a medical record
# Endpoint: POST / (relative to router prefix, e.g., /medical/)
@router.post("/")
def add_record(
    
    # data:
    # Request Body -> Validated using MedicalRecordCreate Schema
    data: MedicalRecordCreate,
    
    # db: 
    # Injecting database session using Depends
    # get_db() will automatically provide DB connection
    db: Session = Depends(get_db),
    
    # current_user:
    # Injecting logged-in user using Depends
    # get_current_user() handles authentication logic
    current_user = Depends(get_current_user)
):
    
    # Calling service layer method
    # Passes DB session, logged-in user, and request data
    return service.create_record(db, current_user, data)

# GET API -> Fetch medical records of a user
# Endpoint: GET /{user_id}
@router.get("/{user_id}")
def get_records(
    
    # user_id:
    # Path parameter -> extracted from URL
    # Example: /medical/5 -> user_id = 5
    user_id: int,
    
    # Injecting DB session
    db: Session = Depends(get_db),
    
    # Injecting current user
    current_user = Depends(get_current_user)
):
    
    # Calling service layer to fetch records
    return service.get_records(db, current_user, user_id)