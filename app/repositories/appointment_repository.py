# Import Session class from SQLAlchemy ORM
# Session = database connection object used to interact with DB (executes queries, transactions)
from sqlalchemy.orm import Session

# Import Appointment model (ORM model mapped to appointments table in DB)
from app.models.appointment import Appointment

# Repository Pattern class:
# - This class is responsible for handling all database operations related to Appointment
# Helps in separating database logic from business logic (clean architecture)
class AppointmentRepository:
    
    # Create method
    # Used to insert a new appointment into the database
    # db: Session -> active database session/connection
    # appointment: Appointment -> ORM object (row to be inserted)
    def create(self, db: Session, appointment: Appointment):
        
        # add() -> stage the object for insertion into DB (does not execute immediately)
        db.add(appointment)
        
        # commit() -> permanently save changes (Insert query executed here)
        # Transaction gets committed
        db.commit()
        
        # refresh() -> reloads the object from DB
        # Useful to get auto-generated values (like id, timestamps)
        db.refresh(appointment)
        
        # return the newly created appointment object
        return appointment
    
    # GET APPOINTMENTS BY USER
    # Fetch all appointments where user is either patient or doctor
    def get_by_user(self, db: Session, user_id: int):
        
        # query(Appointment) -> SELECT * FROM appointment
        # filter() -> applies WHERE conditions
        return db.query(Appointment).filter(
            
            # Condition 1: Appointment.patient_id == user_id
            # Condition 2: Appointment.doctor_id == user_id
            
            # | -> OR operator in SQLAlchemy (logical OR)
            # MEANS: fetch records where user is either patient or doctor
            (Appointment.patient_id == user_id) |
            (Appointment.doctor_id == user_id)
            
            # all() -> fetch all matching records as a list
        ).all()

    # CHECK DOCTOR AVAILABILITY
    # Checks if doctor already has an appointment at given time
    def check_availability(self, db: Session, doctor_id: int, date_time):

        # query(Appointment) → selecting from Appointment table
        return db.query(Appointment).filter(

            # Condition 1: same doctor
            Appointment.doctor_id == doctor_id,

            # Condition 2: same date and time
            Appointment.date_time == date_time,

            # Condition 3: status must be "booked"
            # Only consider active/booked appointments
            Appointment.status == "booked"

        # first() → returns first matching record OR None
        # Used for existence check (faster than all())
        ).first()


    # DELETE APPOINTMENT
    # Removes appointment from database
    def delete(self, db: Session, appointment: Appointment):

        # delete() → marks object for deletion (not executed yet)
        db.delete(appointment)

        # commit() → executes DELETE query and persists changes
        db.commit()