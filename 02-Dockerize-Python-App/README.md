# Dockerized Python Calculator with MariaDB

A containerized Python Flask calculator application integrated with MariaDB, using Docker and Docker Compose for deployment and management.

## Project Overview

This project demonstrates how to containerize a Python web application and deploy it alongside a MariaDB database using Docker Compose.

The application supports basic arithmetic operations and stores calculation history in a persistent MariaDB database.

## Architecture

```text
              User / Browser
                    |
                    |
              Host Port 8082
                    |
                    v
         +---------------------+
         |   Flask Web App     |
         |  Docker Container   |
         |      Port 5000      |
         +---------------------+
                    |
              Docker Network
                    |
                    v
         +---------------------+
         |     MariaDB         |
         |  Docker Container   |
         |      Port 3306      |
         +---------------------+
                    |
                    v
         +---------------------+
         |   Docker Volume     |
         | Persistent Storage  |
         +---------------------+
