# Import SQLAlchemy session
from sqlalchemy.orm import Session

# Import model
from app.models.medical_record import MedicalRecord


class MedicalRepository:

    # Create a medical record
    def create_record(self, db: Session, user_id: int, title: str, description: str):
        """
        Create a new medical record for a user
        """

        record = MedicalRecord(
            user_id=user_id,
            title=title,
            description=description
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        return record


    # Get all records of a user
    def get_records_by_user(self, db: Session, user_id: int):
        """
        Fetch all medical records for a specific user
        """

        return db.query(MedicalRecord).filter(
            MedicalRecord.user_id == user_id
        ).all()


    # Get record by ID
    def get_record_by_id(self, db: Session, record_id: int):
        """
        Fetch a single medical record
        """

        return db.query(MedicalRecord).filter(
            MedicalRecord.id == record_id
        ).first()


    # Update medical record
    def update_record(self, db: Session, record_id: int, title: str = None, description: str = None):
        """
        Update record details
        """

        record = self.get_record_by_id(db, record_id)

        if not record:
            return None

        # Update fields if provided
        if title:
            record.title = title

        if description:
            record.description = description

        db.commit()
        db.refresh(record)

        return record


    # Delete medical record
    def delete_record(self, db: Session, record_id: int):
        """
        Delete a medical record
        """

        record = self.get_record_by_id(db, record_id)

        if not record:
            return False

        db.delete(record)
        db.commit()

        return True