# Importing Appointment model (ORM object)
from app.models.appointment import Appointment

# Importing repository -> handles DB operations
from app.repositories.appointment_repository import AppointmentRepository


# Service layer -> contains business logic
class AppointmentService:
    
    # Constructor -> receives DB Session
    def __init__(self, db):
        
        # Initialize repository with DB Session
        self.repo = AppointmentRepository(db)
        
    # Method for Book Appointment
    def book_appointment(self, patient_id, doctor_id, date_time):
        
        """
        Create a new appointment with validation
        """
        
        # Check if doctor already has an appointment at this time
        existing = self.repo.get_by_doctor_and_time(doctor_id, date_time)
        
        # If slot is already booked -> raise error
        if existing:
            
            # Raise error of doctor not available
            raise Exception("Doctor not available at this time")
        
        # Create Appointment ORM object
        appointment = Appointment(
            
            # Patient booking appointment
            patient_id = patient_id,
            
            # Doctor Assigned
            doctor_id = doctor_id,
            
            # Appointment time
            date_time = date_time,
            
            # Default status
            status = "booked"            
        )
        
        # Save appointment using repository
        return self.repo.create(appointment)
    
    # Get appointments for user
    def get_appointments(self, user):
        
        # Fetch all appointments where user is patient or doctor
        return self.repo.get_by_user(user.id)
    
    # Cancel Appointment (soft delete)
    def cancel_appointment(self, appointment_id: int):
        """
        Cancel appointment by updating status
        """
        
        # Fetch appointment by ID
        appointment = self.repo.get_by_id(appointment_id)
        
        # If not found -> raise error of "Appointment not found"
        if not appointment:
            raise Exception("Appointment not found")
        
        # Update status instead of deleting (soft delete pattern)
        appointment.status = "cancelled"
        
        # Commit changes to DB
        self.repo.db.commit()
        
        # Refresh object to get updated state
        self.repo.db.refresh(appointment)
        
        # Return updated appointment
        return appointment
    
    # Delete Appointment (hard delete)
    def delete_appointment(self, appointment_id: int):
        
        # Fetch appointment
        appointment = self.repo.get_by_id(appointment_id)
        
        # If not found -> raise error
        if not appointment:
            raise Exception("Appointment not found")
        
        # Call repository delete method
        self.repo.delete (appointment)
        
        # Return success response
        return {"message": "Appointment deleted successfully"}