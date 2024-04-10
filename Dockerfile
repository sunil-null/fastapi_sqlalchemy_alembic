# Pull base image
FROM python:3.10-slim

# Set environment varibles
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# Set the Current Working Directory inside the container.
WORKDIR /app

# Upgrading pip.
RUN pip install --upgrade pip

# Download all dependencies.
COPY requirements.txt /app/

# Install all dependencies.
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy current directory into working directory.
COPY . /app

EXPOSE 8000
