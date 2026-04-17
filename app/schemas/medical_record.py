# Importing BaseModel from Pydantic
# BaseModel is used to define data schemas and validate input/output data
from pydantic import BaseModel

# Importing datetime to handle data and time values
from datetime import datetime

# Schema for creating a new medical record (Input schema)
# This is used when client sends data (POST request)
class MedicalRecordCreate(BaseModel):
    
    # user_id:
    # int -> expects an integer value
    # Represents the ID of the user (foreign key reference)
    user_id: int
    
    # title:
    # str -> string type
    # Title of the medical record(e.g. "Blood Test Report")
    title: str
    
    # description:
    # str -> string type
    # Detailed information about the medical record
    description: str
    
# Schema for returning medical record data (output schema)
# This is used when sending response back to client
class MedicalRecordResponse(BaseModel):
    
    # id: 
    # int -> unique identifier of the record
    id: int
    
    # user_id:
    # int -> Id of the associated user
    user_id: int
    
    # title:
    # str -> record title
    title: str
    
    # description:
    # str -> record details
    description: str
    
    # created_at:
    # datetime -> timestamp when record was created
    created_at: datetime
    
    # Config class:
    # Used to configure Pydantic model behavior
    class Config:
        
        # orm_mode = True:
        # Allows Pydantic to read data from ORM objects (like SQLAlchemy models)
        # Without this, it only accepts dictionaries
        # With this, directly return SQLAlchemy objects in FastAPI
        orm_mode = True
        