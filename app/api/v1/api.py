# Import APIRouter → used to combine multiple route groups
from fastapi import APIRouter

# Import all endpoint modules
from app.api.v1.endpoints import (
    auth,
    users,
    doctors,
    appointments,
    medical_records,
    ai,
    health
)

# Create main API router
# This acts as a central place to include all endpoint modules
api_router = APIRouter()


# ---------------- AUTH ROUTES ----------------
# /auth/register
# /auth/login
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)


# ---------------- USER ROUTES ----------------
# /users/me
# /users/update
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)


# ---------------- DOCTOR ROUTES ----------------
api_router.include_router(
    doctors.router,
    prefix="/doctors",
    tags=["Doctors"]
)


# ---------------- APPOINTMENT ROUTES ----------------
# /appointments/book
# /appointments
api_router.include_router(
    appointments.router,
    prefix="/appointments",
    tags=["Appointments"]
)


# ---------------- MEDICAL RECORD ROUTES ----------------
# /records
api_router.include_router(
    medical_records.router,
    prefix="/records",
    tags=["Medical Records"]
)


# ---------------- AI ROUTES (PHASE 7) ----------------
# /ai/analyze
api_router.include_router(
    ai.router,
    prefix="/ai",
    tags=["AI Analysis"]
)


# ---------------- HEALTH CHECK ----------------
# /health
api_router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)