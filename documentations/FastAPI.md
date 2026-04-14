# FastAPI Documentation

A comprehensive guide to building modern, fast APIs using FastAPI.

---

## Introduction

FastAPI is a modern, high-performance web framework for building APIs
with Python using type hints.

---

## Why FastAPI?

Ext- remely fast (comparable to Node.js & Go)
- Uses Python type hints for validation
- Automatic request parsing & response validation
- Built-in interactive API docs

---

## Installation

Install FastAPI along with an ASGI server like Uvicorn:

``` bash
pip install fastapi uvicorn
```

---

## First API

Create first API using FastAPI:

``` python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

Run the server:
```bash
uvicorn main:app --reload
```

Access the API
- Open browser → http://127.0.0.1:8000
- Swagger UI → http://127.0.0.1:8000/docs

---

## Async Server Gateway Interface (ASGI)

* A standard for handling async requests.
* Handles many requests at once (High Performance).
* FastAPI runs on ASGI Servers like Uvicorn
* **Uvicorn** - lightweight, high performance web servers that runs Python's FastAPI apps and handles async incoming HTTP requests.

---


## Path Parameters

Path parameters allow you to pass dynamic values in the URL.

``` python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

**Example Request**
GET /items/10

**Response**
{"item_id": 10}

**How it works?**
- `{item_id}` → dynamic part of the URL
- `item_id:` int → type validation using Python hints
- Automatically parsed and validated by FastAPI

---

## Query Parameters

Query parameters are optional values passed in the URL after ?.

``` python
@app.get("/items/")
def read_item(q: str | None = None):
    return {"q": q}
```

**Example Request**
GET /items/?q=phone

**Response**
{"q": "phone"}

**How it works?**
- `q` → query parameter name
- `str | None` → optional parameter
- `= None` → default value if not provided
- Automatically handled by FastAPI

---

## Request Body

FastAPI allows you to send data in the request body using models defined with Pydantic.

``` python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item
```

**Example Request**
POST /items/

{
  "name": "Laptop",
  "price": 50000
}

**Response**
{
  "name": "Laptop",
  "price": 50000.0
}

**How it works?**
- Request body is automatically parsed as JSON
- Data is validated using Pydantic
- Types are converted if possible (int → float)
- Invalid data raises clear errors

---

## Response Model

FastAPI allows you to define the structure of the response using `response_model`.

**What is `response_model`?**
- Defines the shape of the output
- Ensures only specified fields are returned
- Uses Pydantic for validation

``` python
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    return item
```

**Example Request**
POST /items/

{
  "name": "Laptop",
  "price": 50000
}

**Response**
{
  "name": "Laptop",
  "price": 50000.0
}

**Why use Response Models?**
- Filters sensitive data
- Ensures consistent API responses
- Automatically validates output

---

## Status Codes

FastAPI allows you to set HTTP status codes for responses using the status module.

``` python
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item
```

**What this means?**
- HTTP_201_CREATED → Resource successfully created
- Automatically returned with the response
- Improves API clarity and standards

|  Code  | Name                  | Meaning                 |
| ------ | --------------------- | ----------------------- |
| `200`  | OK                    | Successful request      |
| `201`  | Created               | Resource created        |
| `400`  | Bad Request           | Invalid input           |
| `401`  | Unauthorized          | Authentication required |
| `404`  | Not Found             | Resource not found      |
| `500`  | Internal Server Error | Server error            |

---

## Dependency Injection

FastAPI provides a powerful way to manage dependencies using Depends.

``` python
from fastapi import Depends

def get_db():
    return "DB Connection"

@app.get("/")
def read_root(db = Depends(get_db)):
    return {"db": db}
```

**What is Dependency Injection?**
- A way to reuse common logic (e.g., DB, auth, config)
- Injects required components into your route functions
- Managed automatically by FastAPI

**How it works?**
- Depends(get_db) → calls get_db()
- Result is passed as parameter (db)
- No manual function calls needed

---

## Running Server

Start your FastAPI application using Uvicorn:

``` bash
uvicorn app.main:app --reload
```

- `uvicorn` → ASGI server
- `app.main` → Python file (app/main.py)
- `app` → FastAPI instance inside the file
- `--reload` → Auto-restarts server on code changes

---

## Best Practices

-   Use Pydantic for validation
-   Keep routes modular
-   Use dependency injection
-   Follow clean architecture

---