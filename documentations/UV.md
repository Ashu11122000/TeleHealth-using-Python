# UV (Ultra Fast Python Package Manager) Documentation

A comprehensive guide to using UV for fast Python package management and
dependency handling.

---

## Introduction

UV is a fast Python package manager written in Rust. It is designed to replace traditional tools like:

- pip (package installation)
- pip-tools (dependency management)
- virtualenv (environment management)

with a single high-performance tool.

---

## Why UV?
- Extremely fast (written in Rust)
- All-in-one tool (install, manage deps, create environments)
- Deterministic and reproducible installs
- Simplifies Python development workflow

---

## Key Features
- Fast dependency installation
- Lockfile-based dependency management
- Built-in virtual environment handling
- Compatible with existing Python projects

---

## Installation

Install UV using pip:

``` bash
pip install uv
```

Verify Installation:
```bash
uv --version
```

---

## Basic Usage

UV provides a familiar interface similar to pip, but with much faster performance.

``` bash
uv pip install requests
```

- Installs the requests library
- Resolves dependencies quickly
- Uses UV’s optimized backend for faster installs

---

## Why Use uv pip?
- Much faster than traditional pip
- Drop-in replacement (same commands)
- Better dependency resolution

---

## Virtual Environment

UV makes it easy to create and manage virtual environments without needing virtualenv.

**Create Environment**

This creates a .venv directory in your project.

``` bash
uv venv
```

**Activate**

``` bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

---

## Installing Packages

You can install Python packages using UV just like pip, but with much better performance.

``` bash
uv pip install fastapi
```

**What this does?**
- Installs the FastAPI framework
- Automatically resolves and installs dependencies
- Uses UV’s high-speed backend for faster installation

---

## Requirements Management

UV provides powerful tools to manage dependencies, similar to pip-tools but faster and more integrated.

**Install from requirements.txt**
Installs all dependencies listed in the file.

``` bash
uv pip install -r requirements.txt
```

**Compile dependencies**
Converts a high-level requirements.in into a fully resolved requirements.txt with pinned versions.

``` bash
uv pip compile requirements.in
```

**Sync environment**
Ensures your environment exactly matches requirements.txt:

- Installs missing packages
- Removes extra packages

``` bash
uv pip sync requirements.txt
```

---

## Dependency Resolution

UV uses a fast and efficient dependency resolver to handle complex dependency trees quickly and accurately.

Dependency resolution ensures:

- All required packages are installed
- Compatible versions are selected
- Conflicts are avoided

**Why UV is better?**
- Extremely fast resolver (written in Rust)
- Handles large dependency graphs efficiently
- Produces consistent and reproducible results

**Without Proper Resolution**
- Version conflicts (e.g., package A needs v1, package B needs v2)
- Broken environments
- Runtime errors

---

## Caching Mechanism

UV caches downloaded packages and dependencies locally, which significantly speeds up repeated installations.

**How it works?**
- First install → packages are downloaded from the internet
- Stored in a local cache
- Next install → reused from cache (no re-download)

**Benefits**
- Much faster repeated installations
- Reduces network usage
- Improves developer productivity

---

## UV vs pip

| Feature          | UV         | pip            | Reason                   |
| ---------------- | ---------- | -------------- | ------------------------ |
| Speed            | Very Fast  | Slower         | Rust vs Python           |
| Dependency       | Built-in   | Limited        | Better resolver          |
| Virtual Env      | Built-in   | Separate       | One tool vs many         |
| Parallel Install | Yes        | No             | Concurrent vs sequential |
| Caching          | Advanced   | Basic          | Better reuse             |
| Lock Files       | Built-in   | Not native     | No extra tools           |
| Reproducibility  | Strong     | Weaker         | Deterministic installs   |
| Ease of Use      | All-in-one | Multiple tools | Simpler workflow         |
| Large Projects   | Excellent  | Slower         | Faster resolution        |

---

## UV vs Poetry

| Feature    | UV        | Poetry    | Reason         |
| ---------- | --------- | --------- | -------------- |
| Speed      | Very Fast | Moderate  | Rust vs Python |
| Complexity | Simple    | Higher    | Less config    |
| Lock File  | Yes       | Yes       | Both support   |
| Dependency | Strong    | Strong    | Modern tools   |

---

## Best Practices

-   Use UV for faster installs
-   Maintain requirements.txt
-   Use virtual environments
-   Keep dependencies minimal

---
