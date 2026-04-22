# Import APIRouter & dependencies
# APIRouter -> used to define route groups
# Depends -> for dependency injection
# HTTPException -> for proper API error handling
from fastapi import APIRouter, Depends, HTTPException

# Import SQLAlchemy Session -> DB connection
from sqlalchemy.orm import Session

# Import DB dependency -> provides DB session per request
from app.db.session import get_db

# Import auth dependency -> return currently logged-in user
from app.api.deps import get_current_user

# Import request and response schemas (Pydantic models)
from app.schemas.appointment import AppointmentCreate, AppointmentResponse

# Import service layer -> contains business logic
from app.services.appointment_service import AppointmentService


# Create router with prefix "/appointments"
# All endpoints will start with /appointments
router = APIRouter(prefix="/appointments", tags=["Appointments"])

# Book appointments
@router.post("/book", response_model=AppointmentResponse)
def book_appointment(
    
    # Request body (Validated automatically)
    data: AppointmentCreate,
    
    # Inject DB Session
    db: Session = Depends(get_db),
    
    # Inject logged-in user
    current_user = Depends(get_current_user)
):
    
    # Initialize service with DB session
    service = AppointmentService(db)

    try:
        
        # Call service method to book appointment
        return service.book_appointment(
            
            # Passing full user object
            patient=current_user,
            
            # Doctor ID from request
            doctor_id=data.doctor_id,
            
            # Appointment time
            date_time=data.date_time
        )
        
    # Handle business errors
    except Exception as e:
        
        # Convert Python exception -> HTTP response
        raise HTTPException(status_code=400, detail=str(e))


# Get User Appointments
@router.get("/", response_model=list[AppointmentResponse])
def get_appointments(
    
    # Inject DB
    # Inject user
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    
    # Initialize service
    service = AppointmentService(db)
    
    # Fetch appointments where user is patient or doctor
    return service.get_appointments(current_user)


# Cancel appointment (Soft delete)
@router.delete("/{appointment_id}", response_model=AppointmentResponse)
def cancel_appointment(
    
    # Path parameter
    appointment_id: int,
    
    # Inject DB
    db: Session = Depends(get_db),
    
    # Inject user
    current_user = Depends(get_current_user)
):
    
    # Initialize service
    service = AppointmentService(db)

    try:
        
        # Cancel appointment (status -> "cancelled")
        return service.cancel_appointment(appointment_id)
    
    # If appointment not found -> return 404
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))