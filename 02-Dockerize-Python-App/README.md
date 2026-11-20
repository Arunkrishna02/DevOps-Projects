# Dockerized Python Calculator with MariaDB

A containerized Python Flask calculator application integrated with MariaDB, deployed using Docker and Docker Compose.

This project demonstrates containerization of a Python web application, multi-container communication, database integration, persistent storage, environment configuration, and container management.

## Project Overview

The application provides basic arithmetic operations through REST API endpoints and stores calculation history in a MariaDB database.

Docker Compose is used to manage the Flask application and MariaDB database as separate containers.

## Architecture

```text
                 User / Browser
                       |
                       |
                 Host Port 8082
                       |
                       v
             +--------------------+
             |   Flask Web App    |
             |  Docker Container  |
             |     Port 5000      |
             +--------------------+
                       |
                       |
                Docker Network
                       |
                       v
             +--------------------+
             |      MariaDB       |
             |  Docker Container  |
             |     Port 3306      |
             +--------------------+
                       |
                       |
                       v
             +--------------------+
             |   Docker Volume    |
             | Persistent Storage |
             +--------------------+
```

## Technologies Used

- Python
- Flask
- MariaDB
- Docker
- Docker Compose
- Docker Networking
- Docker Volumes
- Linux
- REST API

## Project Structure

```text
02-Dockerize-Python-App/
├── app.py
├── web_app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## Prerequisites

Ensure the following tools are installed:

- Docker
- Docker Compose
- Git

Verify Docker installation:

```bash
docker --version
docker compose version
```

## Configuration

Create the environment configuration file:

```bash
cp .env.example .env
```

Edit the `.env` file:

```env
DB_NAME=calculator
DB_USER=calculator_user
DB_PASSWORD=change_this_password
DB_ROOT_PASSWORD=change_this_root_password
DB_PORT=3306
APP_PORT=8082
```

Environment variables are used to configure the application and database without hardcoding credentials in the source code.

> Never commit your `.env` file to GitHub.

## Deployment

Clone the repository:

```bash
git clone https://github.com/Arunkrishna02/DevOps-Projects.git
```

Navigate to the project directory:

```bash
cd DevOps-Projects/02-Dockerize-Python-App
```

Build the Docker images and start the containers:

```bash
docker compose up -d --build
```

Check the running containers:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs -f web
```

View database logs:

```bash
docker compose logs -f db
```

## Access the Application

The application runs on:

```text
http://localhost:8082
```

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Application homepage |
| `/add?a=10&b=5` | GET | Addition |
| `/subtract?a=10&b=5` | GET | Subtraction |
| `/multiply?a=10&b=5` | GET | Multiplication |
| `/health` | GET | Application health check |
| `/history` | GET | Retrieve calculation history |

### API Examples

Addition:

```bash
curl "http://localhost:8082/add?a=100&b=50"
```

Expected response:

```json
{
  "a": 100.0,
  "b": 50.0,
  "operation": "addition",
  "result": 150.0
}
```

Subtraction:

```bash
curl "http://localhost:8082/subtract?a=100&b=50"
```

Multiplication:

```bash
curl "http://localhost:8082/multiply?a=10&b=5"
```

Health check:

```bash
curl "http://localhost:8082/health"
```

Calculation history:

```bash
curl "http://localhost:8082/history"
```

## Docker Architecture

### Application Container

The Flask application runs inside a Docker container built using the project's Dockerfile.

The application container communicates with the MariaDB container through the Docker network using the database service name.

### Database Container

MariaDB runs in a separate container and stores calculation history.

The application connects to the database using the following configuration:

```text
DB_HOST=db
DB_PORT=3306
```

Docker Compose provides internal DNS resolution, allowing the application to access the database using the hostname `db`.

### Persistent Storage

A Docker volume is used to persist database data.

```text
calculator-db-data
```

Database data remains available even if the database container is removed and recreated.

## Useful Docker Commands

List running containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

Follow application logs:

```bash
docker compose logs -f web
```

Stop the application:

```bash
docker compose stop
```

Start stopped containers:

```bash
docker compose start
```

Stop and remove containers:

```bash
docker compose down
```

Rebuild the application:

```bash
docker compose up -d --build
```

## Database Persistence

The MariaDB database uses a Docker volume to store data independently of the container lifecycle.

This allows database records to survive container removal and recreation.

List Docker volumes:

```bash
docker volume ls
```

Inspect the database volume:

```bash
docker volume inspect calculator-db-data
```

## Troubleshooting

### Application container is not running

Check the container status:

```bash
docker compose ps
```

Check application logs:

```bash
docker compose logs web
```

### Database connection failure

Check database status:

```bash
docker compose logs db
```

Verify that the database container is healthy:

```bash
docker compose ps
```

### Port already in use

If port `8082` is already occupied, change `APP_PORT` in your `.env` file.

For example:

```env
APP_PORT=8083
```

Then recreate the containers:

```bash
docker compose down
docker compose up -d
```

## Cleanup

Stop and remove the application containers:

```bash
docker compose down
```

To remove the database volume and permanently delete stored database data:

```bash
docker volume rm calculator-db-data
```

> Warning: Removing the database volume permanently deletes the stored calculation history.

## Learning Outcomes

Through this project, I gained hands-on experience with:

- Containerizing a Python Flask application.
- Writing and building Dockerfiles.
- Managing multi-container applications using Docker Compose.
- Configuring applications using environment variables.
- Container-to-container communication through Docker networking.
- Integrating a Flask application with MariaDB.
- Managing persistent storage using Docker volumes.
- Using health checks to monitor container status.
- Troubleshooting Docker containers and application connectivity.
- Documenting and deploying containerized applications.

