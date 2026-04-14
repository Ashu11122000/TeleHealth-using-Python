# Python Dotenv Documentation

A comprehensive guide to using python-dotenv for managing environment
variables in Python applications.

---

## Introduction

python-dotenv is a library that allows you to load environment variables
from a `.env` file into your application.

---

## Why Use dotenv?
- Keeps secrets (API keys, passwords) secure
- Separates configuration from code
- Easy environment management (dev, test, prod)
- Simplifies local development

---

## Installation

``` bash
pip install python-dotenv
```

---

## Setup .env File

Create a `.env` file in your project root:

``` env
APP_NAME=MyApp
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/db
```

---

## Loading Environment Variables

``` python
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")
print(db_url)
```

- `.env` file contains key-value pairs
- `load_dotenv()` loads them into environment variables
`os.getenv()` retrieves the values

---

## Accessing Variables

You can access environment variables in Python using the built-in os module.

``` python
import os

app_name = os.getenv("APP_NAME")
print(app_name)
```

- `os.getenv("KEY")` retrieves the value of an environment variable
- Returns None if the variable is not set
- Works with both system environment variables and `.env` files

---

## Default Values

You can provide a default value when accessing environment variables using `os.getenv().`

``` python
debug = os.getenv("DEBUG", "False")
```

- If `DEBUG` is set → its value is returned
- If `DEBUG` is not set → "False" is used as default

---

## Overriding Variables

By default, load_dotenv() does not override existing environment variables.

``` python
load_dotenv(override=True)
```

- If a variable already exists in the system → it won’t be changed by default
- With `override=True` → values from .env replace existing variables
- Default behavior is safe (no override)
- Use `override=True` when you want .env to take priority
- Useful in development environments

---

## Using with Pydantic

You can combine dotenv with Pydantic’s BaseSettings to automatically load and validate environment variables.

```env
APP_NAME=MyApp
```

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
print(settings.app_name)
```

* Reads values from:
   - `.env` file
   - System environment variables
* Automatically maps:
   - `APP_NAME` → app_name
* Validates types using Pydantic

---

## Best Practices

-   Never commit `.env` files to Git
-   Use `.env.example` for sharing structure
-   Keep sensitive data secure
-   Use environment-specific configs

---

## Conclusion

python-dotenv simplifies environment variable management and improves
application security and configuration handling.
