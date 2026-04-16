# Import Appointment ORM Model (represents appointments table in DB)
from app.models.appointment import Appointment

# Import Repository class (handles DB operations)
from app.repositories.appointment_repository import AppointmentRepository

# Service Layer Class
# This layer contains business logic (rules, validations, workflows)
# It sits between API (FastAPI routes) and Repository (DB Layer)
class AppointmentService:
    
    # Constructor (Called when object is created)
    def __init__(self):
        
        # creating instance of repository
        # This allows to interact with database via repo methods
        self.repo = AppointmentRepository()
        
    # Book Appointment Method
    # Handles logic for creating a new appointment
    def book_appointment(self, db, patient, doctor_id, date_time):
        
        # Step 1: Check availability 
        # Prevents double booking for same doctor and time
        existing = self.repo.check_availability(db, doctor_id, date_time)
        
        # If an appointment already exists -> raise error
        if existing:
            
            # Stop execution and sends error response
            raise Exception("Doctor not available at this time")
        
        # Step 2: Create Appointment object (ORM instance)
        # This is not saved yet - just a Python object
        appointment = Appointment(
            
            # patient_id -> comes from authenticated user object
            # Foreign Key mapping (patient_id column in DB)
            patient_id = patient.id,
            
            # doctor_id -> passed from API request
            doctor_id = doctor_id,
            
            # date_time -> appointment time
            date_time = date_time
        )
        
        # Step 3: Save appointment using repository
        # Repository handles DB insert logic
        return self.repo.create(db, appointment)
    
    # GET APPOINTMENT FOR USER
    # Fetch all appointments where user is involved (patient or doctor)
    def get_appointment(self, db, user):
        
        # user.id -> unique identifier of logged-in user
        return self.repo.get_by_user(db, user.id)
    
    # CANCEL APPOINTMENT
    # Soft delete approach (status update instead of removing record)
    def cancel_appointment(self, db, appointment):
        
        # Update status field instead of deleting from DB
        # "cancelled" -> business state change
        appointment.status = "cancelled"
        
        # commit() -> persist changes to database
        # Executes UPDATE query
        db.commit()
        
        # Return updated appointment object
        return appointment