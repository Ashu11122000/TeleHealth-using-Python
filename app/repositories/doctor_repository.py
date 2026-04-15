# Import SQLAlchemy session
from sqlalchemy.orm import Session

# Import model
from app.models.doctor_profile import DoctorProfile


class DoctorRepository:

    # Create doctor profile
    def create_doctor_profile(self, db: Session, user_id: int, specialization: str, experience: int):
        """
        Create a doctor profile linked with user
        """

        doctor = DoctorProfile(
            user_id=user_id,
            specialization=specialization,
            experience=experience
        )

        db.add(doctor)
        db.commit()
        db.refresh(doctor)

        return doctor


    # Get doctor profile by user_id
    def get_doctor_by_user_id(self, db: Session, user_id: int):
        """
        Fetch doctor profile using user ID
        """

        return db.query(DoctorProfile).filter(
            DoctorProfile.user_id == user_id
        ).first()


    # Get doctor by doctor_profile ID
    def get_doctor_by_id(self, db: Session, doctor_id: int):
        """
        Fetch doctor using doctor profile ID
        """

        return db.query(DoctorProfile).filter(
            DoctorProfile.id == doctor_id
        ).first()


    # Get all doctors
    def get_all_doctors(self, db: Session):
        """
        Fetch all doctors
        """

        return db.query(DoctorProfile).all()


    # Update doctor profile
    def update_doctor_profile(self, db: Session, doctor_id: int, specialization: str = None, experience: int = None):
        """
        Update doctor profile details
        """

        doctor = self.get_doctor_by_id(db, doctor_id)

        if not doctor:
            return None

        # Update only if values provided
        if specialization:
            doctor.specialization = specialization

        if experience is not None:
            doctor.experience = experience

        db.commit()
        db.refresh(doctor)

        return doctor