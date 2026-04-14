# FastAPI: A modern Python web framework for building APIs
from fastapi import FastAPI  

# CORSMiddleware: Handles Cross-Origin Resource Sharing (CORS)
# Allows frontend (different origin) to access backend
from fastapi.middleware.cors import CORSMiddleware  

# NEW: Import API router (this connects all endpoints like /auth)
from app.api.v1.api import api_router  


# Create FastAPI app instance
app = FastAPI(
    
    # title: Name of your API (visible in docs)
    title="Telehealth Backend",
    
    # version: API version for tracking changes  
    version="1.0.0"  
)

# CORS CONFIGURATION
# CORS setup
origins = [
    "http://localhost:3000",   # React frontend (local)
    "http://127.0.0.1:3000"   # Alternative localhost
]

app.add_middleware(
    # Middleware layer that processes requests before reaching routes
    CORSMiddleware,

    # Allowed frontend origins
    allow_origins=origins,  
    
    # Allows cookies and auth headers (important for JWT later)
    allow_credentials=True, 
    
    # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_methods=["*"],
    
    # Allows all headers (Authorization, Content-Type, etc.)
    allow_headers=["*"],  
)

# ROUTER REGISTRATION (VERY IMPORTANT)
# This connects all API routes (like /auth/register, /auth/login)
# Without this, your endpoints will NOT work
app.include_router(api_router)

# ROOT ENDPOINT (HEALTH CHECK)
# Defines a GET endpoint at "/"
@app.get("/")  
def root():
    
    # Returns JSON response
    return {"message": "Telehealth API running"}