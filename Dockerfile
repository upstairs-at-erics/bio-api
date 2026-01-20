# Use the official Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies for MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project code
COPY . /app/

# Remove local sqlite and venv
RUN rm -f db.sqlite3 && rm -rf venv

# Expose the port
EXPOSE 8000

# Start Gunicorn
# "bio.wsgi:application" refers to your bio/wsgi.py file
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "bio.wsgi:application"]