# Importing APIRouter → used to create modular API routes
# Depends → used for dependency injection (like DB session, auth, etc.)
from fastapi import APIRouter, Depends

# Importing Session → SQLAlchemy database session
from sqlalchemy.orm import Session

# Importing request & response schemas (data validation using Pydantic)
from app.schemas.ai import AIAnalysisRequest, AIAnalysisResponse

# Importing service layer (business logic)
from app.services.ai_service import AIService

# Importing dependencies:
# get_db → provides database session
# get_current_user → provides authenticated user
from app.api.deps import get_db, get_current_user


# Creating a router instance → helps organize routes into modules
router = APIRouter()


# Creating a POST endpoint at "/analyze"
# response_model → ensures response follows AIAnalysisResponse schema
@router.post("/analyze", response_model=AIAnalysisResponse)
def analyze_symptoms(
    
    # Request body → validated using AIAnalysisRequest schema
    request: AIAnalysisRequest,

    # Injecting database session automatically using Depends
    db: Session = Depends(get_db),

    # Injecting current logged-in user (authentication)
    current_user = Depends(get_current_user)
):
    """
    This API endpoint:
    - Receives symptoms from user
    - Calls service layer to analyze risk
    - Returns risk level and summary
    """

    # Calling service layer function (business logic)
    result = AIService.analyze_symptoms(
        db,                    # Database session
        current_user.id,       # Logged-in user's ID
        request.symptoms       # List of symptoms from request body
    )

    # Returning result → FastAPI automatically converts it to JSON
    # Also validates response using AIAnalysisResponse schema
    return result