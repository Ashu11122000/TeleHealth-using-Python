# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Copy dependency files
COPY pyproject.toml /app/

# Install dependencies (using pip for simplicity)
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv passlib[bcrypt] python-jose

# Copy project
COPY . /app

# Expose port
EXPOSE 8000

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]