# Import CryptContext for hashing passwords securely (bcrypt, etc.)
from passlib.context import CryptContext

# Import JWT tools (encode/decode + error handling)
from jose import JWTError, jwt

# Import datetime utilities to handle token expiration
from datetime import datetime, timedelta

# Import project settings (SECRET_KEY, ALGORITHM, EXPIRY, etc.)
from app.core.config import settings

# Create password hashing context
pwd_context = CryptContext(
    
    # Use bcrypt hashing algorithm
    schemes = ["bcrypt"],
    
    # Automatically upgrade old hashes if needed
    deprecated = "auto"
)

# Function to hash a plain password before storing in DB
def hash_password(password: str) -> str:
    
    # Take plain password -> return hashed version
    return pwd_context.hash(password)

# Function to verify password during login 
def verify_password(plain_password: str, hashed_password: str) -> bool:
    
    # Compares plain password with hashed password from DB
    return pwd_context.verify(plain_password, hashed_password)

# Function to create JWT access token
def create_access_token(data: dict):
    
    # Copy the original data (to avoid modifying original dict)
    to_encode = data.copy()
    
    # Create expiration time (current time + configured minutes)
    expire = datetime.utcnow() + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Add expiration ("exp") field into payload
    to_encode.update({ "exp": expire })
    
    # Encoded JWT token
    encoded_jwt = jwt.encode(
        
        # Payload (user data)
        to_encode,
        
        # Secret key for signing
        settings.SECRET_KEY,
        
        # Algorithm (e.g., HS256)
        algorithm = settings.algorithm
    )
    
    # Return generated token
    return encoded_jwt

# Function to decode JWT token (used in protected routes)
def decode_access_token(token: str):
    try:
        
        # Decode token using same secret + algorithm
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY,
            algorithms = [settings.ALGORITHM]
        )
        
        # Return decoded data (user info)
        return payload
    except JWTError:
        
        # If token is invalid/expired -> return None
        return None
    
