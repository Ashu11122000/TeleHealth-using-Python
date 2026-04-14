# Pydantic Documentation

A comprehensive guide to using Pydantic for data validation and settings
management in Python.



---

## Introduction to Pydantic

Pydantic is a Python library used for data validation and parsing using
Python type hints.

* **Pydantic** = **Data Validation** + **Data Parsing**

**Why Pydantic?**
- Enforces type safety
- Automatically converts data types
- Very fast (built on Python)
- Widely used with FastAPI for API development
- Pydantic is like a smart gatekeeper
   - It checks data coming from any API, file etc. is correct or not?
   - If yes - it converts
   - If no -> throws a clear message

**Data Parsing**
Process of analyzing, breaking down and converting the raw, unstructured data into a readable, structured format (like JSON) that software can easily understand.

| Without Pydantic   | With Pydantic        |
| ------------------ | -------------------- |
| Manual validation  | Automatic validation |
| More bugs          | Cleaner & safer code |
| Extra code         | Less boilerplate     |


---

## Installation

Install Pydantic using pip:

``` bash
pip install pydantic
```

---

## Basic Usage

Pydantic uses Python type hints to define data models and automatically validates input data.

``` python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Ashish", age=22)
print(user)
```

---

## Type Hints

Tells Python and Pydantic: **What type of data should be here?**

```python
name: str
age: int
price: float
is_active: bool
```

Python interpreter reads data types internally but do not print data types in output.

---

## BaseModels

* Foundation of Pydantic
* Defines data types
* Add **type rules** - using standard Python type hints and the **field() function** for added **constraints**.
* Automatically validate + convert data
* **field() function** uses to provide metadata and validation constraints for model fields beyond their basic type annotations.
* **Constraints** are the conditions or rules that a variable must satisfy for a solution or program to be considered valid.

```python
from pydantic import BaseModel

class User(BaseModel):

    # Reuse print of data
    name: str
    age: int

# Valid input and work fine
user = User(name = "Ashish", age = 25)
print(user)

# Field with default value required (default value for age)
user = User(name = "Ashish")
print(user)
```

---

## Data Validation

Data Validation is a process of ensuring data is clean, correct, and useful before it is processed, stored and analyzed.

Pydantic automatically validates and converts input data based on the defined types.

``` python
from pydantic import BaseModel

class User(BaseModel):
    age: int

User(age="25")  # Automatically converts to int
```

**How it works?**
- "25" (string) ➝ converted to 25 (integer)
- Pydantic tries to coerce compatible types automatically
- If conversion fails, it raises a ValidationError

---

## Field Types

Pydantic supports standard Python data types for defining model fields.

``` python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool
```

| Type    | Description                | Example Input      |
| ------- | -------------------------- | ------------------ |
| `str`   | Text/String                | `"Laptop"`         |
| `int`   | Integer                    | `10`               |
| `float` | Decimal number             | `99.99`            |
| `bool`  | Boolean (`True` / `False`) | `"true"` → `True`  |
| `list`  | List of items              | `[1, 2, 3]`        |
| `dict`  | Key-value pairs            | `{"key": "value"}` |


---

## Default Values

You can assign default values to fields in a Pydantic model. If no value is provided, the default will be used.

``` python
class User(BaseModel):
    name: str
    active: bool = True
```

---

## Nested Models

Pydantic allows you to create models inside other models, making it easy to represent complex and structured data.

**Automatic Parsing**
- You can pass a dictionary for nested fields
- Pydantic automatically converts it into the corresponding model (Address)

``` python
class Address(BaseModel):
    city: str

class User(BaseModel):
    name: str
    address: Address
```

---

## Model Methods

Pydantic models provide built-in methods to easily convert and work with data.

``` python
user.dict()
user.json()
```

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Ashish", age=22)

print(user.dict())
print(user.json())
```

---

## Settings Management

Pydantic provides a powerful way to manage configuration using environment variables via BaseSettings.

``` python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
```

**How it works?**
- Reads values from environment variables
- Automatically maps APP_NAME → app_name
- Validates and converts data types

---

## Environment Variables

Pydantic automatically reads values from environment variables and maps them to model fields.

``` python
class Settings(BaseSettings):
    database_url: str

settings = Settings()
```

**How it works?**
- Converts field name `database_url` → environment variable `DATABASE_URL`
- Automatically loads value at runtime
- Validates type (str in this case)

---

## Error Handling

Pydantic raises a ValidationError when input data does not match the expected types or constraints.

``` python
from pydantic import ValidationError

try:
    User(age="abc")
except ValidationError as e:
    print(e)
```

---

## Custom Validator

Pydantic allows you to define custom validation logic using @field_validator (Pydantic v2).

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    age: int

    @field_validator("age")
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Age must be at least 18")
        return value
```

---

## Error Customization
You can customize validation errors to make them more user-friendly.

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    age: int

    @field_validator("age")
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("You must be 18+ to register")
        return value
```

---

## @model_validator (Cross-Field Validation)

Use @model_validator when validation depends on multiple fields together.

```python
from pydantic import BaseModel, model_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
```

---

## Best Practices

-   Use type hints properly
-   Keep models simple
-   Use BaseSettings for configs
-   Validate input data strictly

