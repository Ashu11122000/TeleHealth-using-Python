# Import APIRouter → used to create modular route groups in FastAPI
# Import Depends → used for Dependency Injection (automatic resource/provider injection)
from fastapi import APIRouter, Depends

# Import Session → SQLAlchemy database session (DB connection handler)
from sqlalchemy.orm import Session

# Import dependency functions:
# get_db → provides DB session
# get_current_user → provides authenticated user
from app.api.deps import get_db, get_current_user

# Import Pydantic schema → used for request validation
from app.schemas.appointment import AppointmentCreate

# Import Service layer → contains business logic
from app.services.appointment_service import AppointmentService


# Create router instance
# APIRouter helps organize endpoints (like /appointments, /users, etc.)
router = APIRouter()

# Create service instance
# This will call business logic methods
service = AppointmentService()


# BOOK APPOINTMENT ENDPOINT
# POST → used to create new resource
@router.post("/book")
def book_appointment(

    # data → request body (validated by Pydantic schema)
    data: AppointmentCreate,

    # db → injected database session using Depends
    db: Session = Depends(get_db),

    # current_user → injected authenticated user
    current_user = Depends(get_current_user)
):

    # Call service layer method
    # Pass DB, user, doctor_id, date_time
    return service.book_appointment(
        db, current_user, data.doctor_id, data.date_time
    )


# GET APPOINTMENTS ENDPOINT
# GET → used to retrieve data
@router.get("/")
def get_appointments(

    # Inject DB session
    db: Session = Depends(get_db),

    # Inject authenticated user
    current_user = Depends(get_current_user)
):

    # Fetch appointments where user is patient or doctor
    return service.get_appointments(db, current_user)


# CANCEL APPOINTMENT ENDPOINT
# DELETE → used to remove or cancel resource
@router.delete("/{appointment_id}")
def cancel_appointment(

    # Path parameter → extracted from URL (/123)
    appointment_id: int,

    # Inject DB session
    db: Session = Depends(get_db),

    # Inject authenticated user
    current_user = Depends(get_current_user)
):

    # Fetch appointment from DB
    # query(Appointment) → SELECT * FROM appointments
    # get(id) → fetch record by primary key
    # NOTE: get() is legacy, better to use db.get(Appointment, id)
    appointment = db.query(Appointment).get(appointment_id)

    # Call service to cancel appointment
    return service.cancel_appointment(db, appointment)