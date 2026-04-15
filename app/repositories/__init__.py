# Import all repositories

from .user_repository import UserRepository
from .appointment_repository import AppointmentRepository
from .doctor_repository import DoctorRepository
from .medical_repository import MedicalRepository
from .ai_repository import AIRepository

# Define what is publicly available
__all__ = [
    "UserRepository",
    "AppointmentRepository",
    "DoctorRepository",
    "MedicalRepository",
    "AIRepository"
]