# Base image
FROM python:3-slim


WORKDIR /app

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev  # Install PostgreSQL client libraries


# upgrading pip
RUN pip install --upgrade pip 

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# copy requirements file and install dependencies
COPY requirements.txt ./

# Install psycopg2 with specific flags and environment variables
RUN LIBRARY_PATH=/usr/local/lib:/usr/lib pip install psycopg2==2.9.9

RUN pip install --no-cache-dir -r requirements.txt


#copy the rest of the project files
COPY . .

# Expose the server port
EXPOSE 8000

# Command to start the server
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]