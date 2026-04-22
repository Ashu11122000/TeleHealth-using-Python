# Import Session class from SQLAlchemy ORM
# Session -> manages DB connection, queries, and transactions
from sqlalchemy.orm import Session

# Import Appointment model (maps to appointments table)
from app.models.appointment import Appointment

# Import datetime for handling date-time fields
from datetime import datetime

# Repository class -> handles all DB operations for Appointment
class AppointmentRepository:
    
    # Constructor -> receives DB session (dependency injection)
    def __init__(self, db: Session):
        
        # Store DB session for reuse
        self.db = db

    # Create appointment
    def create(self, appointment: Appointment):
        """
        Insert a new appointment into DB
        """
        
        # Add object to session (staging insert)
        self.db.add(appointment)
        
        # Commit transaction -> executes INSERT query
        self.db.commit()
        
        # Refresh object -> Fetch updated DB values (like auto ID)
        self.db.refresh(appointment)
        
        # Return created appointment
        return appointment

    # Get appointment by ID
    def get_by_id(self, appointment_id: int):
        
        # SELECT * FROM appointments WHERE id = appointment_id
        return self.db.query(Appointment).filter(
            Appointment.id == appointment_id
        ).first()    # Return single record or None

    # Get appointments for a user (patient or doctor)
    def get_by_user(self, user_id: int):
        
        # Fetch appointments where user is either patient or doctor
        return self.db.query(Appointment).filter(
            
            # OR condition using | operator
            (Appointment.patient_id == user_id) |
            (Appointment.doctor_id == user_id)
        ).all()    # Returns list of records

    # Check doctor availability at a specific time
    def get_by_doctor_and_time(self, doctor_id: int, date_time: datetime):
        """
        Returns existing appointment if slot is already booked
        """
        return self.db.query(Appointment).filter(
            
            # Same doctor
            Appointment.doctor_id == doctor_id,
            
            # Same date and time
            Appointment.date_time == date_time,
            
            # Only consider booked appointments
            Appointment.status == "booked"
        ).first()    # Used for conflict checking

    # Get all appointments (optional but useful)
    def get_all(self):
        
        # SELECT * FROM appointments
        return self.db.query(Appointment).all()

    # Delete appointment
    def delete(self, appointment: Appointment):
        
        # Mark object for deletion
        self.db.delete(appointment)
        
        # Commit transaction -> executes DELETE query
        self.db.commit()