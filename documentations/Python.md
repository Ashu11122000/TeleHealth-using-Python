# Python Complete Guide (Beginner to Advanced)

A comprehensive guide covering Python from basics to advanced concepts with theory and practical examples.

---

# Introduction

Python is a high-level, interpreted programming language known for readability and simplicity.

Python is a general-purpose programming that allows to write programs quickly with fewer lines of code compared to languages like C++ or Java.

Simple syntax:
```python
print("Hello World")
```

- High-level data structures
- Effective approach to object-oriented programming
- Ideal language for scripting
- Available on Windows, Mac, & Linux

---

# Features:
- **Easy to learn:** Limited sets of keywords, simple syntax
- **Dynamically Typed:** The data type of variable determined at run time automatically
- **Rich libraries:** Python has thousands of ready-made libraries, so you don’t need to build everything from scratch.
- **Extensible:** Easily add new functionality or integrate code writing in other languages to the core python interpreter without modifying its source code
- **Interactive:** Interpreter immediately returns the response
- **Interpreted:** Code executed dynamically at runtime, rather than being fully translated into standalone execution machine code
- **Database Connectivity:** Almost any type of database can be used with Python application

---

# Interactive Python (IPython)

- Enhanced and powerful interactive environment in Python
- Python uses it as its main kernel
- Highlighting keywords, variables, etc.
- Ability to check properties of an object during runtime
- History internally stored and reused
- Controlling Python environment and performing OS Tasks

---

# Installation & Setup

- Go to the official website: https://www.python.org
- Download latest Python version
- Run installer
- IMPORTANT: Check
- Add Python to PATH
- Click Install Now
- Verify installation of Python:
```bash
python --version
```

---

# Virtual Environment:

A virtual environment is an isolated space where you can install project-specific dependencies without affecting your system Python.

- Allows users to be install packages and modifying their python environment
- Considered as disposable
- Used to contain a specific python interpreter 
- Contained in a directory, conventionally either named venv or .venv
- Not considered as moveable or copyable

**Why important?**

- Avoid version conflicts
- Clean project management
- Professional practice

```bash
python -m venv .venv
```

- Activating Virtual Environment
```bash
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

---

# Identifier

- Name used to identify a variable, function, module, class, etc.
- Starts with A to Z or a to z or underscore(_) followed with 0 or more letters, underscore and digits (0 to 9)
- Python class starts with uppercase. Other identifiers with lower cases.
- Identifier starting with single underscore(_) is **private identifier**
- Identifier starting with double underscore (__) is **strongly private identifier**

---

# Lines and Indentation

- Python provides no braces to indicate block of codes for class and function definitions of flow control.

- Block of codes are denoted by line indentation, which is rigidly enforced.

```python
if True:
    print("True")
else:
    print("False")
```

---

# Comments

- Programmer-readable explanation in the Python source code
- Purpose of making the source code for easier to understand
- Ignored by Python interpreter
- using Hash sign (#) for comments
- A line containing only whitespaces, possibly with a comment is known as a blank line and Python totally ignores it.

---

# Variables 

* Reserved memory locations used to store values within a program.
* Whenever a variable is created, it reserves some space in memory.
* Memory space allocated to variable based on data type of a variable.
* Computer's memory locations are having a number or address, internally represented in binary form.
* Once a variable stored in memory, it should be accessible repeatedly by other processes easily.

```python
name = "Ashish"    # String
age = 22    # integer
height = 5.9    # float
is_student = True    # boolean

print(name)
print(age)
print(height)
print(is_student)
```

**Variable Accessibility**
* **Public:** Can be accessible anywhere.
* **Protected:** Can be accessible within block.
* **Private:** Accessible by once itself.

---

# Private Variables

* Special type of variables that are only accessible within the class they are defined in.
* Not accessible outside the class.
* Only direct access is restricted.

```python
class Person:
    def __init__(self, name, age):
        self.name = name    # public variable
        self.__age = age    # private variable

p = Person("Ashish", 22)

print(p.name)    # accessible
print(p.__age)    # Cannot access private variable
```

* **Getter Method** is a public method access the private variable outside the class.
* **Setter Method** is a public method used to modified the value of a private variable outside the class.

```python
class Person:
    def __init__(self, age):
        self.__age = age   # private variable

    # Getter method
    def get_age(self):
        return self.__age

    # Setter method
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

p = Person(22)

print(p.get_age())   # ✅ 22

p.set_age(25)
print(p.get_age())   # ✅ 25

p.set_age(-5)        # ❌ Invalid
```

* Private variables are defined by adding (__) double underscore before the variable name. 
* Example: __init__ is a special method called as initializers, that runs automatically every time whenever a new object of a class is created.

```python
class Person:
    def __init__(self, name, age):
        self.__age = age
    
    def get_age(self):
        return self.__age

p = Person("Ashish", 22)
print(p.get_age())
```

* In Python, private variables are not truly private
   - Still accessed from outside the class using a technique called mangling.
   - As private variables using double underscore (__), Python internally changes it in `_classname__var`.
   - Now, this private variable easily accessible outside the function/class.

---

# Data Types

| Type   | Description                  | Example        | Code              | Notes                     |
|--------|------------------------------|----------------|-------------------|---------------------------|
| int    | Whole numbers                | `10`, `-5`     | `x = 10`          | No size limit             |
| float  | Decimal numbers              | `3.14`, `-2.5` | `pi = 3.14`       | Supports `1e3`            |
| str    | Text (characters)            | `"Ashish"`     | `name = "Ashish"` | `' '` or `" "` allowed    |
| bool   | True/False values            | `True/False`   | `is_valid = True` | Used in conditions        |

---

# Operators

Operators are symbols used to perform operations on variables and values.

* **Arithmetic Operators**

| Operator | Meaning        | Example   | Result |
|----------|----------------|-----------|--------|
| +        | Addition       | 5 + 3     | 8      |
| -        | Subtraction    | 5 - 3     | 2      |
| *        | Multiplication | 5 * 3     | 15     |
| /        | Division       | 5 / 2     | 2.5    |
| //       | Floor Division | 5 // 2    | 2      |
| %        | Modulus        | 5 % 2     | 1      |
| **       | Exponent       | 2 ** 3    | 8      |

* **Comparison Operator**

| Operator | Meaning              | Example   | Result |
|----------|----------------------|-----------|--------|
| ==       | Equal to             | 5 == 5    | True   |
| !=       | Not equal            | 5 != 3    | True   |
| >        | Greater than         | 5 > 3     | True   |
| <        | Less than            | 5 < 3     | False  |
| >=       | Greater or equal     | 5 >= 5    | True   |
| <=       | Less or equal        | 3 <= 5    | True   |

* **Logical Operator**

| Operator | Meaning      | Example              | Result |
|----------|--------------|----------------------|--------|
| and      | Both true    | True and False       | False  |
| or       | Any true     | True or False        | True   |
| not      | Reverse      | not True             | False  |

* **Assignment Operators**

| Operator | Meaning             | Example   | Equivalent |
|----------|---------------------|-----------|------------|
| =        | Assign              | x = 5     | —          |
| +=       | Add & assign        | x += 3    | x = x + 3  |
| -=       | Subtract & assign   | x -= 2    | x = x - 2  |
| *=       | Multiply & assign   | x *= 2    | x = x * 2  |
| /=       | Divide & assign     | x /= 2    | x = x / 2  |
| //=      | Floor divide assign | x //= 2   | x = x // 2 |
| %=       | Modulus assign      | x %= 2    | x = x % 2  |
| **=      | Power assign        | x **= 2   | x = x ** 2 |

* **Identity Operator**

| Operator | Meaning               | Example        | Result |
|----------|-----------------------|----------------|--------|
| is       | Same object           | x is y         | True/False |
| is not   | Not same object       | x is not y     | True/False |

* **Membership Operator**

| Operator | Meaning              | Example            | Result |
|----------|----------------------|--------------------|--------|
| in       | Value exists         | 'a' in 'apple'     | True   |
| not in   | Value not exists     | 'b' in 'apple'     | False  |

* **Bitwise Operator**

| Operator | Meaning       | Example   | Result |
|----------|---------------|-----------|--------|
| &        | AND           | 5 & 3     | 1      |
| |        | OR            | 5 | 3     | 7      |
| ^        | XOR           | 5 ^ 3     | 6      |
| ~        | NOT           | ~5        | -6     |
| <<       | Left Shift    | 5 << 1    | 10     |
| >>       | Right Shift   | 5 >> 1    | 2      |

---

# Conditional Statements

- Conditional statements allow your program to make decisions based on conditions (True/False).

- They control the flow of execution.

Example:

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

**1. if statement**
- Executes block only when condition is True.

```python
age = 20

if age >= 18:
    print("You are eligible to vote")
```

**2. if-else statement**
- One block runs if True, another if False.
```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

**3. if-elif-else statement**
- Used when checking multiple conditions.

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

**4. Nested if**
- if inside another if.
```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
```

| Type        | Description                | Example Condition | Use Case                  |
|-------------|----------------------------|-------------------|---------------------------|
| if          | Runs if condition is True  | age >= 18         | Simple decision           |
| if-else     | Two outcomes               | age >= 18         | Binary decision           |
| if-elif     | Multiple conditions        | marks >= 60       | Grading, categories       |
| nested if   | Condition inside condition | age + ID check    | Complex validations       |

---

# Loops

- Loops are used to repeat a block of code multiple times until a condition is met.

- They help avoid writing repetitive code.

**1. For Loop**

Used when you know how many times to iterate.

Example:
```python
for i in range(5):
    print(i)
```

**2. for-else Loop**

- runs after loop completes normally
- Does NOT run if loop is stopped using break

```python
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Loop finished")
```

**3. While Loop**
- Used when the number of iterations is unknown.
- Runs until condition becomes False.

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

| Loop Type | Description                     | Example Condition | Use Case              |
|-----------|---------------------------------|-------------------|-----------------------|
| for       | Fixed iterations                | range(5)          | Known count loops     |
| for-else  | Runs else after completion      | no break used     | Search/check patterns |
| while     | Runs until condition is False   | x < 5             | Unknown iterations    |

---

# Loop Control Statements in Python

Loop control statements are used to **control the flow of loops** by altering their normal execution.

**Types of Loop Control Statements**

- `break` → Stops the loop completely  
- `continue` → Skips current iteration  
- `pass` → Does nothing (placeholder)

**1. `break` Statement**

The `break` statement is used to exit the loop immediately, even if the loop condition is still True.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

**2. continue Statement**

The `continue` statement is used to skip the current iteration and move to the next one.

---

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**3. pass Statement**

The `pass` statement is a placeholder that does nothing.  
It is used when a statement is required syntactically but you don’t want to execute any code.

```python
for i in range(5):
    pass
```

| Statement | Purpose        | Effect on Loop         | Use Case                  |
| --------- | -------------- | ---------------------- | ------------------------- |
| break     | Exit loop      | Stops loop immediately | Stop when condition met   |
| continue  | Skip iteration | Skips current step     | Ignore specific values    |
| pass      | Do nothing     | No effect              | Placeholder / empty block |


---

# Functions

Functions are reusable blocks of code used to perform a specific task.  
They help make code modular, readable, and maintainable.

A function:
- Is defined using the `def` keyword
- Can take inputs (parameters)
- Can return output using `return`
- Can be reused multiple times

**1. Built-in Functions**
Standard library includes built-in functions like print(), len(), sum() etc.

**2. User-define Functions**
Creates our own functions.

**Basic Syntax**

```python
def function_name(parameters):
    # code block
    return value
```

```python
Example:
def greet(name):
    return f"Hello {name}"

print(greet("Ashish"))
```

| Part     | Description                |
| -------- | -------------------------- |
| `def`    | Keyword to define function |
| `greet`  | Function name              |
| `name`   | Parameter (input)          |
| `return` | Sends value back to caller |

**Types of Functions**

* Function with Parameters & Return

```python
def add(a, b):
    return a + b
```

* Function without Return

```python
def greet():
    print("Hello")
```

* Function without Parameters

```python
def welcome():
    return "Welcome!"
```

* **Default Parameters**
Python allows to define a function with a default value assigned to one or more formal arguments.

```python
def greet(name="Guest"):
    return f"Hello {name}"

print(greet())        # Guest
print(greet("Ashish"))
```

* **Keyword Arguments**

Allows to pass function arguments in the form of keywords also known as named arguments.

```python
def intro(name, age):
    print(name, age)

intro(age=22, name="Ashish")
```

**Function Parameters**
* **1. Call By Value:** 
- A copy of original values of one function directly passes to the parameters/arguments of another function
- Original values are not affected
- Uses more memory
- Safer, Protected original data

* **2. Call By References:**
- Variable's address/reference of one function passes as parameters/arguments of another function
- Original values are affected
- Uses less memory
- data should be changeable

* **Functional arguments**
- Values or variables passed into a function when it is called.
- The behavior of a function depends on the arguments passed in it.

* **Positional Arguments**
List of variables declared in the parentheses at the time of defining a function are the formal arguments.

* **Arbitrary Arguments (*args)**
(might be positional or keyword arguments) define a function that is able to accept arbitrary or variable number of arguments.

---

# Data Structures in Python

- Data structures are used to store, organize, and manage data efficiently.  
- Python provides built-in data structures that are powerful and easy to use.

**Types of Data Structures**

1. List  
2. Tuple  
3. Set  
4. Dictionary  

**1. List**

- A list is an ordered, mutable (changeable) collection of elements
- Allows duplicate values  
- Indexed (supports indexing & slicing)  
- Defined using `[]`
- `len()` - returns the number of elements in the list
- `insert()` - add item at specific index
- `extend()` - add multiple elements in a list at once
- `remove()`- removes items from list by its value
- `pop()` - remove item from list by its index
- `del`- also removes item from list by its index
- `slicing` - list[start:end]
- `sort()` - arrange items in lists in ascending/descending order
- `reverse()` - reverse lists
- `split()` - Converts string into list
- `join()` - Converts list into string

```python
numbers = [1, 2, 3, 4]
numbers.append(5)

print(numbers)
```

**2. Tuple**

- A tuple is an ordered, immutable (unchangeable) collection.
- Accessing elements/data items using index
- Actually using tuple as a key inside a dictionary
- Allows duplicates
- Cannot be modified after creation
- Defined using ()

```python
t = (1, 2, 3)
print(t[0])
```

**3. Set**

- A set is an unordered collection of unique elements
- Order doesn't matter in sets
- No duplicates allowed
- Not indexed
- Defined using {}

```python
s = {1, 2, 3, 3}
print(s)
```

**4. Dictionary**

- A dictionary stores data in key-value pairs.
- Keys must be unique
- Values can be any type
- Defined using {key: value}

```python
user = {
    "name": "Ashish",
    "age": 22
}

print(user["name"])
```

---

# String

* Immutable sequence of UNICODE characters.
* Each character has a unique numeric value.
* `\n` - new line
* `\s` - space
* `\t` - tab
* `&plus;` - Concatenation of two strings
* `*` - Repetition - Creates new string / concatenating multiple copies of same string
* `[]` - Slice - Gives the character from the given index of string
* `[:]` - Range slice - Gives the characters from the given range
* **f"string** - called as f-string (formatted string literal) which inserts variables and expressions directly into a string using {}.

```python
name = "Ashish"
print(f"Hello {name}")
```

---

# File Handling in Python

- File handling allows you to create, read, write, and manage files in Python.  
- It is commonly used for data storage, logging, and processing external data.
- Python provides built-in functions to work with files.
- The most common function:

```python
open(filename, mode)
```

**File Modes**
| Mode | Description                       |
| ---- | --------------------------------- |
| `r`  | Read file (default)               |
| `w`  | Write (overwrite file)            |
| `a`  | Append (add to file)              |
| `x`  | Create new file (error if exists) |

```python
# Writing to a file
with open("file.txt", "w") as f:
    f.write("Hello World")

# Reading from a file
with open("file.txt", "r") as f:
    print(f.read())
```

---

# Exception Handling in Python

* Exception handling is used to handle runtime errors gracefully without crashing the program.
* An exception is an error that occurs during program execution.
* Instead of stopping the program, Python allows you to:
   -  Catch the error
   - Handle it properly
   - Continue execution

**Basic Syntax**

```python
try:
    # code that may cause error
except ExceptionType:
    # code to handle error
finally:
    # always runs (optional)
```

**Example**
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
```

| Block    | Purpose                       |
| -------- | ----------------------------- |
| `try`    | Code that may raise exception |
| `except` | Handles the exception         |
| `else`   | Runs if no exception occurs   |
| `finally`| Always executes               |

---

# Modules & Packages in Python

Modules and packages help you organize code into reusable files and folders.  
They make your code modular, scalable, and maintainable.

* **Module**
A module is a single Python file (`.py`) that contains functions, variables, or classes.

Example:
- `math.py` - built-in module - (comes with Python standard library)
- `mymodule.py` - custom module - (created by user)

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

* **Package**
- A **package** is a folder that contains multiple modules.
- It helps in organizing large projects.

```python
from utils import add, to_lower

print(add(10, 5))
print(to_lower("HELLO"))
```

**Importing Modules**
*Example (Built-in Module)*

```python id="a9k2zp"
import math

print(math.sqrt(16))
```

---

# Object-Oriented Programming (OOP) in Python

- OOP is a programming paradigm that uses objects and classes to structure code.  
- It helps in building modular, reusable, and scalable applications.

**Core Concepts**

- Class  
- Object  
- Inheritance  
- Encapsulation  
- Polymorphism  

**1. Class**
- A **class** is a blueprint for creating objects.  
- It defines properties (variables) and behaviors (methods).

```python
class Person:
    def __init__(self, name):
        self.name = name
```

**2. Object**
An **object** is an instance of a class.  
It represents a real-world entity and contains:
- Data (attributes)
- Behavior (methods)

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ashish")  # object creation
print(p.name)
```

**3. Inheritance**
- Inheritance allows a class (child class) to inherit properties and methods from another class (parent class).
- Helps in code reuse and reducing duplication

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Inheriting from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # inherited method
d.bark()
```

**4. Encapsulation**

- Encapsulation is one of the core principles of Object-Oriented Programming (OOP).  
- It is used to hide internal data and control access to it.

**Encapsulation means:**
* Wrapping data (variables) and methods into a single unit (class)
* Restricting direct access to some components
* Achieved using:
   - **Private variables** (`__variable`)
   - **Getter & Setter methods**

---

**Why Use Encapsulation?**

- Protect sensitive data  
- Prevent accidental modification  
- Control how data is accessed or updated  
- Improve code maintainability  

```python
class Person:
    def __init__(self, age):
        self.__age = age   # private variable

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

p = Person(22)

print(p.get_age())   # Access using getter

p.set_age(25)        # Modify using setter
print(p.get_age())
```

**5. Polymorphism**

- Polymorphism is a core concept of Object-Oriented Programming (OOP).  
- It allows the same method or function name to behave differently based on the object or data type.

* **Poly** = many, **morph** = forms  
   - Polymorphism means one interface, multiple implementations

**Why Use Polymorphism?**

- Improves code flexibility  
- Enhances readability  
- Reduces code duplication  
- Makes code scalable  

**Types of Polymorphism in Python**

1. Method Overriding  
2. Duck Typing  
3. Operator Overloading  

**1. Method Overriding**

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):   # overriding
        print("Dog barks")

d = Dog()
d.sound()
```

**2. Duck Typing**

```python
class Bird:
    def sound(self):
        print("Chirp")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

make_sound(Bird())
make_sound(Dog())
```

**3. Operator Overloading**

```python
print(5 + 3)        # addition
print("Hi " + "Ashish")  # string concatenation
```

| Type                 | Description                       | Example            |
| -------------------- | --------------------------------- | ------------------ |
| Method Overriding    | Redefine parent method            | Dog → Animal       |
| Duck Typing          | Behavior-based execution          | sound() method     |
| Operator Overloading | Same operator, different behavior | `+` for int/string |


| Concept       | Description                     | Example Use  |
| ------------- | ------------------------------- | ------------ |
| Class         | Blueprint                       | Person       |
| Object        | Instance of class               | p = Person() |
| Inheritance   | Reuse code                      | Dog → Animal |
| Encapsulation | Data hiding                     | __balance    |
| Polymorphism  | Same method, different behavior | sound()      |

---

# Decorators in Python

Decorators are a powerful feature in Python used to modify or extend the behavior of functions without changing their actual code.

A decorator is a function that:
- Takes another function as input  
- Adds extra functionality  
- Returns a new function  

* It follows the concept of higher-order functions

**Why Use Decorators?**

- Code reuse  
- Cleaner and readable code  
- Separation of concerns  
- Useful for logging, authentication, validation  

**Basic Syntax**

```python
def decorator_function(original_function):
    def wrapper():
        # extra work
        original_function()
        # extra work
    return wrapper
```

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
```

---

# Generators & Iterators in Python

Generators and iterators are used to handle sequences of data efficiently, especially when dealing with large datasets.

- **Iterator** → An object that allows you to traverse through elements one by one  
- **Generator** → A special type of iterator created using `yield`

**1. Iterator**
An **iterator** is an object that implements:
- `__iter__()` → returns the iterator object  
- `__next__()` → returns the next value  

```python
numbers = [1, 2, 3]

it = iter(numbers)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
```

**2. Decorators**
Decorators are used to modify or extend the behavior of functions or methods without changing their actual code.

A decorator is a function that:
- Takes another function as input  
- Adds extra functionality before/after it  
- Returns a new function  

* This is possible because functions in Python are first-class objects (they can be passed around like variables)

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
```

| Concept         | Description                             |
| --------------- | --------------------------------------- |
| Decorator       | Function that modifies another function |
| Wrapper         | Inner function that adds behavior       |
| @ syntax        | Cleaner way to apply decorator          |
| *args, **kwargs | Handle any arguments                    |
| wraps()         | Preserve metadata                       |


---

# Lambda (Anonymous Functions) in Python

Lambda functions are small, anonymous (unnamed) functions used for short, one-line operations.

A lambda function:
- Has **no name**
- Can take multiple arguments  
- Contains only **one expression**
- Automatically returns the result  

* Used when you need a function temporarily. 

**Syntax**

```python
lambda arguments: expression
```

**Example**
```python
add = lambda a, b: a + b
print(add(2, 3))
```

---

# List Comprehension 

List comprehension provides a compact and efficient way to create lists in Python.

List comprehension allows you to:
- Write **shorter and cleaner code**
- Replace traditional loops
- Create lists in a **single line**

**Syntax**

```python
[expression for item in iterable if condition]
```

**Example**
```python
squares = [x*x for x in range(5)]
print(square)
```

---

# Standard Libraries

**1. OS Module**
- The os module in Python provides a way to interact with the operating system. 
- It allows you to perform tasks like handling files, directories, environment variables, and system commands.

**Why use the OS module?**
- Work with file & directory paths
- Create, delete, and rename files/folders
- Access environment variables
- Run system-level commands
- Write platform-independent code

```python
import os
print(os.getcwd())
```

| Feature     | os module           | pathlib (modern) |
| ----------- | ------------------- | ---------------- |
| Style       | Functional          | Object-oriented  |
| Readability | Medium              | High             |
| Recommended | Yes (legacy/common) | Preferred        |


**2. Sys Module**
- The sys module in Python provides access to variables and functions that interact directly with the Python runtime environment. 
- It is mainly used for handling command-line arguments, system-specific parameters, and controlling program execution.

**Why use the Sys module?**
- Access command-line arguments
- Exit programs safely
- Work with Python interpreter settings
- Handle input/output streams
- Manage recursion limits and memory

**
```python
import sys
print(sys.argv)
```

---

## Logging Module

The `logging` module in Python is used to track events that happen during program execution. It is a powerful alternative to `print()` statements and is widely used in real-world applications for debugging, monitoring, and auditing.

**Why Use Logging Instead of Print?**

- Provides different severity levels (INFO, DEBUG, WARNING, ERROR, CRITICAL)
- Can write logs to files, streams, or external systems
- Helps in debugging and maintaining large applications
- Easy to disable or filter logs without changing code

**Logging Levels**

| Level      | Description                                      |
|------------|--------------------------------------------------|
| DEBUG      | Detailed information for debugging               |
| INFO       | General information about program execution      |
| WARNING    | Something unexpected but not an error            |
| ERROR      | A serious problem occurred                      |
| CRITICAL   | Very severe error, program may stop             |

**Basic Example**

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")
```

---

## Multithreading

Multithreading allows a program to run multiple threads (smaller units of a process) concurrently. It is useful for tasks that involve waiting (I/O-bound tasks) like network requests, file operations, or user input.

**What is a Thread?**

A **thread** is the smallest unit of execution within a process. Multiple threads share the same memory space, making communication between them faster.

**Why Use Multithreading?**

- Improves performance for I/O-bound tasks
- Enables concurrent execution
- Keeps applications responsive (e.g., UI apps)
- Efficient use of system resources

**Basic Example**

```python
import threading

def task():
    print("Running")

t = threading.Thread(target=task)
t.start()
```

---
