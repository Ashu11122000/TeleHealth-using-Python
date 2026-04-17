# Importing Session -> SQLAlchemy database session
# This is used to perform database operations (CRUD)
from sqlalchemy.orm import Session

# Import MedicalRecord model (represents DB table)
from app.models.medical_record import MedicalRecord

# Repository class
# Handles all direct database interactions 
class MedicalRepository:
    
    # CREATE -> Insert new medical record into DB
    def create_record(self, db: Session, user_id: int, title: str, description: str):
        
        # Creating a new MedicalRecord object (not yet saved in DB)
        record = MedicalRecord(
            user_id = user_id,
            title = title,
            description = description
        )
        
        # db.add() -> Adds object to session (staging area)
        db.add(record)
        
        # db.commit() -> Saves changes permanently in database
        db.commit()
        
        # db.refresh() -> Reloads object from DB (gets updated values like ID)
        db.refresh(record)
        
        # Return the saved record
        return record
    
    # READ -> Get all records for a specific user
    def get_record_by_user(self, db: Session, user_id: int):
        
        # db.query(Model) -> Start query for a table
        # .filter() -> Apply condition (WHERE clause)
        # .all() -> Return all matching rows as list
        return db.query(MedicalRecord).filter(
            MedicalRecord.user_id == user_id
        ).all()
        
    # READ -> Get Single record by its ID
    def get_record_by_id(self, db: Session, record_id: int):
        
        # .first() -> Returns first matching record or None
        return db.query(MedicalRecord).filter(
            MedicalRecord.id == record_id
        ).first()
    
    # Update -> Modify existing record
    def update_record(self, db: Session, record_id: int, title: str = None, description: str = None):
        
        # Fetch record from DB
        record = self.get_record_by_id(db, record_id)
        
        # If record does not exist -> return None
        if not record:
            return None
        
        # Update fields only if new values are provided
        if title is not None:
            record.title = title
        
        if description is not None:
            record.description = description
        
        # Commit changes to database    
        db.commit()
        
        # Refresh object with latest DB State
        db.refresh(record)
        
        # Return updated record
        return record
    
    # DELETE -> Remove record from database
    def delete_record(self, db: Session, record_id: int):
        
        # Fetch record first
        record = self.get_record_by_id(db, record_id)
        
        # If record doesn't exist -> return False
        if not record:
            return False
        
        # db.delete() -> Marks object for deletion
        db.delete(record)
        
        # Commit deletion
        db.commit()
        
        # Return success status
        return True
    