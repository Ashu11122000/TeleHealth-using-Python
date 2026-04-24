# Import Session class fro SQLAlchemy ORM
# Session is used to interact with the database (perform queries, insert, update, delete, transactions)
from sqlalchemy.orm import Session

# Import DoctorProfile model (ORM class mapped to doctor_profiles table in DB)
from app.models.doctor_profile import DoctorProfile

# Repository class (Design Pattern)
# Repository pattern is used to separate database logic from business logic
class DoctorRepository:
    
    # Create doctor profile
    def create_doctor(
        # Refers to current instance of the class
        self,
        
        # Database session (used to interact with DB)
        db: Session,
        
        # Foreign Key (link to user table)
        user_id: int,
        
        # Doctor's specialization (e.g., cardiologist)
        specialization: str,
        
        # Years of experience
        experience: int
        
        # Return type (Returns DoctorProfile object)
    ) -> DoctorProfile:
        
        doctor = DoctorProfile(
            user_id=user_id,
            specialization=specialization,
            experience=experience
        )

        db.add(doctor)
        db.commit()
        db.refresh(doctor)

        return doctor

    # Get doctor by ID
    def get_by_id(self, db: Session, doctor_id: int) -> DoctorProfile | None:
        return db.query(DoctorProfile).filter(
            DoctorProfile.id == doctor_id
        ).first()

    # Get doctor by user ID
    def get_by_user_id(self, db: Session, user_id: int) -> DoctorProfile | None:
        return db.query(DoctorProfile).filter(
            DoctorProfile.user_id == user_id
        ).first()

    # Get all doctors (with optional pagination)
    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10
    ):
        return db.query(DoctorProfile).offset(skip).limit(limit).all()

    # Update doctor profile (safe update)
    def update_doctor(
        self,
        db: Session,
        doctor: DoctorProfile,
        specialization: str | None = None,
        experience: int | None = None
    ) -> DoctorProfile:

        if specialization is not None:
            doctor.specialization = specialization

        if experience is not None:
            doctor.experience = experience

        db.commit()
        db.refresh(doctor)

        return doctor

    # Delete doctor profile
    def delete_doctor(self, db: Session, doctor: DoctorProfile) -> None:
        db.delete(doctor)
        db.commit()