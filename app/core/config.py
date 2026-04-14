# Used to create settings class that reads values from environment variables (.env)
from pydantic_settings import BaseSettings

# Used to cache the settings object (so it's created only once)
# lru_cache (Least recently used cache): A decorator that stores the result of a function
# so that if it's called again, it returns the cached result instead of running again
from functools import lru_cache

# This class defines all configuration variables for application
# It inherits from BaseSettings, so values are automatically loaded from .env
class Settings(BaseSettings):
    
    # DATABASE_URL: A connection string used to connect to database
    # Example Format: postgresql://username:password@host:port/database
    DATABASE_URL: str
    
    # SECRET_KEY: A private key used for cryptographic operations like signing JWT tokens
    # It must be kept secure and never exposed publicly
    SECRET_KEY: str
    
    # ALGORITHM: Refers to the cryptographic hashing algorithm used in JWT
    # HS256 = HMAC (Hash-based Message Authentication Code) using SHA-256
    # It ensures data integrity and authenticity
    ALGORITHM: str = "HS256"
    
    # ACCESS_TOKEN_EXPIRE_MINUTES: Defines how long a JWT token is valid
    # After this time, the user must re-authenticate
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Config: Special inner class used by Pydantic to customize behavior
    class Config:
        # env_file: Specifies that variables should be loaded from a .env file
        env_file = ".env"

# This makes get_settings() behave like a singleton
# Singleton: A design pattern where only one instance of a class is created and reused
@ lru_cache
def get_settings():
    
    # Creates and returns a Settings object
    # Due to caching, this object is created only once and reused everywhere
    return Settings()