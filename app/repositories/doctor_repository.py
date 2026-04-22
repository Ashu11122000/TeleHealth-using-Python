# Import SQLAlchemy session
# Session -> used to interact with the database (queries, transactions)
from sqlalchemy.orm import Session

# Import DoctorProfile model (mapped to doctor_profiles table)
from app.models.doctor_profile import DoctorProfile

# Repository class -> handles all DB Operations for DoctorProfile
class DoctorRepository:
    
    # Constructor -> receives DB session (dependency injection)
    def __init__(self, db: Session):
        
        # Store DB session for reuse
        self.db = db

    # Create doctor profile
    def create(self, user_id: int, specialization: str, experience: int):
        """
        Create a doctor profile linked with a user
        """
        
        # Create ORM object (represents a row in DB)
        doctor = DoctorProfile(
            
            # Foreign Key -> links to user table
            user_id=user_id,
            
            # Doctor's specialization (e.g., cardiologist)
            specialization=specialization,
            
            # Years of experience
            experience=experience
        )
        
        # Add object to session (staging for insert)
        self.db.add(doctor)
        
        # Commit transaction -> executes INSERT query
        self.db.commit()
        
        # Refresh object -> fetch updated values from DB (e.g., auto-generated ID)
        self.db.refresh(doctor)
        
        # Return created doctor profile
        return doctor

    # Get doctor by ID
    def get_by_id(self, doctor_id: int):
        
        # Query DB -> SELECT * FROM doctor_profiles WHERE id = doctor_id
        return self.db.query(DoctorProfile).filter(
            DoctorProfile.id == doctor_id
        ).first()    # Returns one record or None

    # Get doctor by user ID
    def get_by_user_id(self, user_id: int):
        
        # Fetch doctor profile linked to a specific user
        return self.db.query(DoctorProfile).filter(
            DoctorProfile.user_id == user_id
        ).first()

    # Get all doctors
    def get_all(self):
        # Fetch all doctor records
        return self.db.query(DoctorProfile).all()

    # Update doctor profile
    def update(self, doctor: DoctorProfile, data: dict):
        """
        Update doctor profile dynamically
        """
        
        # Loop through input dictionary (key-value pairs)
        for key, value in data.items():
            
            # setattr -> dynamically update attribute
            # Example: setattr(doctor, "experience", 10)
            setattr(doctor, key, value)

        # Commit changes -> executes UPDATE query
        self.db.commit()
        
        # Refresh object -> get latest data from DB
        self.db.refresh(doctor)

        # Return updated doctor object
        return doctor

    # Delete doctor profile
    def delete(self, doctor: DoctorProfile):
        
        # Mark object for deletion
        self.db.delete(doctor)
        
        # Commit Transaction -> executes DELETE query
        self.db.commit()