# FastAPI: A modern Python web framework for building APIs
from fastapi import FastAPI  

# CORSMiddleware: Handles Cross-Origin Resource Sharing (CORS)
# Allows frontend (different origin) to access backend
from fastapi.middleware.cors import CORSMiddleware  
app = FastAPI(
    
    # title: Name of your API (visible in docs)
    title="Telehealth Backend",
    
    # version: API version for tracking changes  
    version="1.0.0"  
)

# CORS setup
origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000"
]

app.add_middleware(
    # Middleware layer that processes requests before reaching routes
    CORSMiddleware,

    # Allowed frontend origins
    allow_origins=origins,  
    
    # Allows cookies and auth headers
    allow_credentials=True, 
    
    # Allows all HTTP methods (GET, POST, etc.)
    allow_methods=["*"],
    
    # Allows all headers
    allow_headers=["*"],  
)

# Defines a GET endpoint at "/"
@app.get("/")  
def root():
    
    # Returns JSON response
    return {"message": "Telehealth API running"}  