# declarative_base: A factory function in SQLAlchemy that creates a base class for all ORM models (tables).
# ORM (Object Relational Mapping) lets interaction with the database using Python classes instead of raw SQL queries 
from sqlalchemy.orm import declarative_base

# Base: This is the parent class for all database models (tables)
# Every model (like User, Product, etc.) will inherit from this Base class
# It helps SQLAlchemy keep track of all tables and map them to the database schema
Base = declarative_base()