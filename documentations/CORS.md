# CORS (Cross-Origin Resource Sharing) Documentation

A comprehensive guide to understanding and implementing CORS in web
applications.

---

## Introduction

CORS (Cross-Origin Resource Sharing) is a security feature implemented
by browsers to control how resources are requested from a different
domain.

---

## What is CORS?

CORS allows a server to specify who can access its resources from a
different origin.

Example: Frontend: http://localhost:3000
Backend: http://localhost:8000

These are different origins.

---

## Why CORS is Needed?

-   Prevents unauthorized access
-   Protects user data
-   Controls cross-origin requests

---

## How CORS Works

Browser sends a `request → Server` responds with `headers → Browser` decides whether to allow it.

---

## Common Headers

-   Access-Control-Allow-Origin
-   Access-Control-Allow-Methods
-   Access-Control-Allow-Headers
-   Access-Control-Allow-Credentials

---

## CORS in FastAPI

``` python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Preflight Requests

Browser sends an OPTIONS request before the actual request to check
permissions.

---

## Allow Origins

``` python
allow_origins=["*"]  # Allows all origins (not recommended for production)
```

---

## Allow Methods & Headers

``` python
allow_methods=["GET", "POST"]
allow_headers=["*"]
```

---

## Common Errors

-   CORS policy blocked request
-   Missing headers
-   Incorrect origin configuration

---

