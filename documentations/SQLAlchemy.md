# SQLAlchemy Documentation

A comprehensive guide to using SQLAlchemy ORM for database interaction
in Python applications.

---

## Introduction

SQLAlchemy is a powerful Python SQL toolkit and Object Relational Mapper
(ORM) that allows developers to interact with databases using Python
classes.

* `SQLAlchemy`- Python library used to interact with databases.
* `Core` - (SQL Expression Language) - Low-level SQL toolkit
   - Lets to write SQL queries using Python code
   - Works with tables and SQL
* `ORM` - **Object Relational Mapper**
   - Technique that lets interaction with a database objects instead of SQL queries.
   - `Database Tables` - Python classes
   - `Rows` - Python objects
   - `SQL Queries` - Python code
---

## Why SQLAlchemy?
- Write database logic using Python objects
- Supports both ORM and raw SQL (Core)
- Works with multiple databases (SQLite, PostgreSQL, MySQL)
- Highly flexible and scalable

---

## Installation

Install SQLAlchemy using uv:

``` bash
uv pip install sqlalchemy
```

Verify Installation:
```bash
python -c "import sqlalchemy; print(sqlalchemy.__version__)"
```

Optional database drivers based on database we used:
```bash
# PostgreSQL
pip install psycopg2-binary

# MySQL
pip install pymysql

# SQLite (built-in with Python, no install needed)
```

---

## Database Connection

SQLAlchemy connects to a database using an Engine, which manages the connection.

**What is an Engine?**
- Core interface to the database
- Manages connections and execution
- Created using `create_engine()`

``` python
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
```

**Database URL**
- `dialect`: Which database we are using?
- `driver`: How Python talks to that database?

```python
dialect+driver://username:password@host:port/database
```

---

## Declaring Models

In SQLAlchemy, models are Python classes that represent database tables.

``` python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
```

**What this means?**
- `Base` → Base class for all models
- `User` → Represents the users table
- Each `class attribute` → A column in the table

**Key Concepts**
- __tablename__ → Table name in database
- Column → Defines table columns
- primary_key=True → Unique identifier
- index=True → Improves query performance

**Declarative Base**
- Base class for all models
- Required ORM for ORM mapping

---

## Creating Tables

SQLAlchemy can automatically create database tables from your models using:

``` python
Base.metadata.create_all(bind=engine)
```

**What it does?
- Reads all models inherited from Base
- Converts them into SQL CREATE TABLE statements
- Creates tables in the connected database

```python
from sqlalchemy import create_engine
from models import Base

engine = create_engine("sqlite:///./test.db")

Base.metadata.create_all(bind=engine)
```

---

## CRUD Operations

### Create

``` python
new_user = User(name="Ashish")
session.add(new_user)
session.commit()
```

### Read

``` python
users = session.query(User).all()
```

### Update

``` python
user.name = "Updated"
session.commit()
```

### Delete

``` python
session.delete(user)
session.commit()
```

---

## Sessions

A Session in SQLAlchemy is used to interact with the database (perform queries, insert, update, delete).

``` python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
```

**What is a Session?**
- Manages database transactions
- Acts as a workspace for ORM operations
- Communicates with the database via the engine

**How it works?**
- Create a session factory → `sessionmaker`
- Create a session instance → `SessionLocal()`
- Use it to perform database operations

**Key Points**
- Each session represents a single unit of work
- Must be closed after use
- Handles transactions automatically

---

## Relationships

SQLAlchemy allows you to define relationships between tables using ForeignKey and relationship.

``` python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")
```

**What this means?**
- `user_id` → Foreign key referencing users.id
- `relationship("User")` → Links Post to User model
- Enables accessing related data easily

**How it works?**
- Each Post belongs to one User
- SQLAlchemy automatically handles joins
- You can access related data via attributes

| Type         | Description                     |
| ------------ | ------------------------------- |
| One-to-Many  | One user → many posts           |
| Many-to-One  | Many posts → one user           |
| One-to-One   | One user → one profile          |
| Many-to-Many | Multiple ↔ multiple (via table) |


---

## Querying Data

You can retrieve data from the database using SQLAlchemy’s query interface.

``` python
user = session.query(User).filter(User.id == 1).first()
```

**What this does?**
- Queries the User table
- Filters where `id == 1`
- Returns the first matching record

---

## Migrations

* Tracks DB Schema changes
* Updates DB safely
* Version Control for Schemas
* Uses **Alembic**
   - Git for database structure
   - Helps to manages and track changes in database schemas over time

---

## Transactions

Group of operations

```python
try:
    session.commit()
except:
    session.rollback()
```

---

## Connection Pooling

- Reuses DB connection
- Faster performance
- Efficient resource code

---

## Loading
- How data being loaded from database?
- ORM decides when to fetch data?

**1. Lazy Loading:** Loads data when needed.
**2. Eager Loading:** Loads data immediately.

---

## Best Practices

-   Use session per request
-   Keep models clean
-   Use migrations (Alembic)
-   Avoid raw SQL when possible

