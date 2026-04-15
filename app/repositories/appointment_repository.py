# Import SQLAlchemy session
from sqlalchemy.orm import Session

# Import Appointment model
from app.models.appointment import Appointment

# Import datetime (for filtering)
from datetime import datetime


class AppointmentRepository:

    # Create a new appointment
    def create_appointment(self, db: Session, patient_id: int, doctor_id: int, date_time: datetime):
        """
        Create a new appointment in database
        """

        # Create Appointment object
        appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date_time=date_time,
            status="scheduled"  # default status
        )

        # Add to DB
        db.add(appointment)

        # Commit changes
        db.commit()

        # Refresh to get updated data
        db.refresh(appointment)

        return appointment


    # Get all appointments of a user (patient or doctor)
    def get_appointments_by_user(self, db: Session, user_id: int):
        """
        Fetch all appointments where user is either patient or doctor
        """

        return db.query(Appointment).filter(
            (Appointment.patient_id == user_id) |
            (Appointment.doctor_id == user_id)
        ).all()


    # Get appointments for a doctor at specific time
    def get_doctor_appointments_by_time(self, db: Session, doctor_id: int, date_time: datetime):
        """
        Used to check availability (service layer will use this)
        """

        return db.query(Appointment).filter(
            Appointment.doctor_id == doctor_id,
            Appointment.date_time == date_time
        ).all()


    # Get appointment by ID
    def get_appointment_by_id(self, db: Session, appointment_id: int):
        """
        Fetch a single appointment
        """

        return db.query(Appointment).filter(
            Appointment.id == appointment_id
        ).first()


    # Update appointment status (cancel, complete, etc.)
    def update_appointment_status(self, db: Session, appointment_id: int, status: str):
        """
        Update appointment status
        """

        appointment = self.get_appointment_by_id(db, appointment_id)

        if appointment:
            appointment.status = status
            db.commit()
            db.refresh(appointment)

        return appointment