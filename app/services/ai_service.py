# Importing the AIRepository class which handles database operations
from app.repositories.ai_repository import AIRepository


# Service layer class (contains business logic, not direct DB queries)
class AIService:

    # Static method → can be called without creating an object of AIService
    @staticmethod
    def analyze_symptoms(db, user_id, symptoms):
        """
        db        → Database session (used to interact with DB)
        user_id   → ID of the user for whom assessment is being created
        symptoms  → List of symptom objects (each has severity like low/medium/high)
        """

        # Initialize score to calculate overall risk level
        score = 0

        # Loop through each symptom in the symptoms list
        for s in symptoms:

            # Check severity of each symptom and assign score accordingly
            if s.severity == "low":
                score += 1   # Low severity adds 1 point

            elif s.severity == "medium":
                score += 2   # Medium severity adds 2 points

            elif s.severity == "high":
                score += 3   # High severity adds 3 points

        # Risk classification logic
        # If total score is 3 or less → Low risk
        if score <= 3:
            risk = "Low"
            summary = "Symptoms appear mild. Monitor your health."

        # If score is between 4 and 6 → Medium risk
        elif score <= 6:
            risk = "Medium"
            summary = "Moderate symptoms. Consider consulting a doctor."

        # If score is greater than 6 → High risk
        else:
            risk = "High"
            summary = "High-risk symptoms. Seek medical attention immediately."

        # Save assessment to database
        # Create a new AI assessment record in DB
        # This function likely inserts data and returns the created object
        assessment = AIRepository.create_assessment(
            db,           # Database session
            user_id,      # User ID
            risk,         # Calculated risk level
            summary       # Generated summary
        )

        # Save all symptoms linked to this assessment
        # assessment.id → foreign key reference
        AIRepository.add_symptoms(
            db,                # Database session
            assessment.id,     # Link symptoms to this assessment
            symptoms           # List of symptoms
        )

        # Return response to API layer
        # Returning result as dictionary (JSON response in API)
        return {
            "risk_level": risk,   # Final calculated risk
            "summary": summary    # Explanation message
        }