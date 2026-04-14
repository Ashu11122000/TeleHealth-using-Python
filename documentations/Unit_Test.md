# Unit Testing Documentation

A comprehensive guide to writing and running unit tests in Python.

---


## Introduction

Unit testing is a software testing method where individual components of
a program are tested independently to ensure they work correctly.

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

---

## Why Unit Testing?

-   Ensures code correctness
-   Prevents bugs
-   Improves code quality
-   Makes refactoring safer

---

## Popular Tools
- `pytest` → Simple and powerful
- `unittest` → Built-in Python testing module

| Feature     | pytest                       | unittest         |
| ----------- | ---------------------------- | ---------------- |
| Ease of Use | Very simple                  | More verbose     |
| Syntax      | Clean & minimal              | Boilerplate code |
| Setup       | Minimal                      | Requires classes |
| Features    | Advanced (fixtures, plugins) | Basic            |
| Built-in    | No                           | Yes              |

---

## Installation

Install pytest using pip and uv:

``` bash
uv pip install pytest
```

OR

```bash
uv add pytest
```

---

## Basic Concepts

### Assertion

Used to check if the result is correct.

``` python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 2) == 4
```

---

### Test Suite

Collection of multiple test cases.

``` python
def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert 5 - 2 == 3
```

---

### Test Runner

Tool that runs tests.

Example: pytest

``` bash
pytest
```

---

### Mocking

Replacing real dependencies with fake ones.

``` python
from unittest.mock import Mock

def test_mock():
    fake_db = Mock()
    fake_db.get_user.return_value = {"name": "Ashish"}
```

---

### Isolation

Each test should run independently.

``` python
def test_one():
    assert True

def test_two():
    assert True
```

---

## Writing Your First Test

``` python
def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 3) == 6
```

---

## Running Tests

``` bash
pytest
```

---

## Best Practices

-   Write small, focused tests
-   Use descriptive test names
-   Avoid external dependencies
-   Use mocking where needed
-   Keep tests independent

---