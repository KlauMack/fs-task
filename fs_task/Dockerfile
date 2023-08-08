FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Set up MySQL configurations
ENV MYSQL_DATABASE=kitchen_magic_db
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword
ENV MYSQL_HOST=db
ENV MYSQL_PORT=3306

# Install the MySQL client for Django to communicate with MySQL database
RUN pip install mysqlclient

# Run Django server (you can modify the command as needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
