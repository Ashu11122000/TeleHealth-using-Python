# create_engine: Creates a connection (engine) to the database
# Engine: Core interface in SQLAlchemy that manages DB connections and executes SQL
from sqlalchemy import create_engine

# sessionmaker: A factory function used to create new database session objects 
# Session: Used to interact with the database (CRUD Operations)
from sqlalchemy.orm import sessionmaker

# Import settings object which contains DATABASE_URL from .env
from app.core.config import settings

engine = create_engine(
    
    # DATABASE_URL: Connection string used to connect to PostgreSQL
    settings.DATABASE_URL,
    
    # echo = True -> Logs all generated SQL queries in the console
    # Useful for debugging and understanding what queries are being executed
    echo = True  # Shows SQL logs
)

# SessionLocal: This is a session factory
# Each time you call SessionLocal(), it creates a new DB session instance
SessionLocal = sessionmaker(
    
    # autocommit: If True, changes are automatically committed to DB
    # False means must manually call session.commit()
    autocommit = False,
    
    # autoflush: Automatically sends changes to DB before query execution
    # False gives you manual control using session.flush()
    autoflush = False,
    
    # bind: Connects this session to the database engine
    bind = engine
)