# Import SQLAlchemy session
from sqlalchemy.orm import Session

# Import models
from app.models.ai_assessment import AIAssessment
from app.models.symptom import Symptom


class AIRepository:

    # Create AI assessment
    def create_assessment(self, db: Session, user_id: int, risk_level: str, summary: str):
        """
        Create AI assessment result
        """

        assessment = AIAssessment(
            user_id=user_id,
            risk_level=risk_level,
            summary=summary
        )

        db.add(assessment)
        db.commit()
        db.refresh(assessment)

        return assessment


    # Add symptoms to an assessment
    def add_symptoms(self, db: Session, assessment_id: int, symptoms: list):
        """
        Add multiple symptoms linked to assessment
        symptoms = [{"name": "...", "severity": "..."}]
        """

        symptom_objects = []

        for symptom in symptoms:
            obj = Symptom(
                assessment_id=assessment_id,
                name=symptom["name"],
                severity=symptom["severity"]
            )
            db.add(obj)
            symptom_objects.append(obj)

        db.commit()

        return symptom_objects


    # Get assessment by ID
    def get_assessment_by_id(self, db: Session, assessment_id: int):
        """
        Fetch AI assessment
        """

        return db.query(AIAssessment).filter(
            AIAssessment.id == assessment_id
        ).first()


    # Get all assessments of a user
    def get_assessments_by_user(self, db: Session, user_id: int):
        """
        Fetch all assessments for a user
        """

        return db.query(AIAssessment).filter(
            AIAssessment.user_id == user_id
        ).all()


    # Get symptoms by assessment ID
    def get_symptoms_by_assessment(self, db: Session, assessment_id: int):
        """
        Fetch symptoms linked to assessment
        """

        return db.query(Symptom).filter(
            Symptom.assessment_id == assessment_id
        ).all()