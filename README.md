# Kitchen Magic

A simple recipe-based web application that allows users to store their favorite recipes and view each others. Web app uses MySQL to store user and their recipe data.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Docker](#docker)
5. [Database](#database)

## Prerequisites

Before you get started, make sure you have the following installed:

- Python 3.8 or up
- Django 3.1 or up
- Docker
- MySQL

## Installation

To run the app locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone (https://github.com/KlauMack/fs-task.git)
2. Change into the project directory:
   ```bash
    cd fs_task
3. Create a virtual environment (optional but recommended):
   ```bash
    python -m venv env
4. Activate the virtual environment:
  - Linux/Mac:
    ```bash
    source env/bin/activate
    ```
  - Windows:
    ```bash
    env\Scripts\activate
    ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
To run the Django app locally, use the following command:
  ```bash
  python manage.py runserver
  ```
Access the app in your web browser at http://localhost:8000.

### Docker
To run the app using Docker, follow these steps:

1. Build the Docker image:
   ```bash
    docker build -t <image_name> .
2. Run the Docker container:
   ```bash
    docker run -p 8000:8000 <image_name>
3. Access the app in your web browser at http://localhost:8000.
   
## Database
To set up the MySQL database, follow these steps:

1. Create the necessary database schema and tables.
2. Modify the `Dockerfile` and `docker-compose.yml` files to connect to your MySQL database.
