# Use the official Python image as the base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production  # Set DJANGO_ENV to 'production'

# Set the working directory inside the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files to the container
COPY pyproject.toml poetry.lock /app/

# Install system dependencies
RUN apt-get update
RUN apt-get install -y curl

# Install Poetry
RUN pip install poetry

# Copy the rest of the application code to the container
COPY . /app/

# Install project dependencies
# Project initialization:



RUN poetry install

# Run migrations
RUN poetry run python manage.py makemigrations
RUN poetry run python manage.py migrate

# Expose the port the application runs on
EXPOSE 8000

# Run the Django server with Unicorn
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
