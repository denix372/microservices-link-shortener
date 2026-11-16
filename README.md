# Microservices Link Shortener

A resilient, multi-tier URL shortener built with Python (FastAPI) and Redis, utilizing a microservices architecture. The application is containerized using Docker Compose and placed behind an NGINX reverse proxy for robust routing.

## 🚀 Features
* **FastAPI Backend:** High-performance REST API for shortening URLs and handling redirects.
* **Redis Database:** Fast, in-memory data store for quick URL resolution.
* **NGINX Reverse Proxy:** Routes incoming traffic efficiently to the backend services.
* **Dockerized:** Fully containerized setup via `docker-compose` for rapid local deployment.
* **CI/CD Pipeline:** Automated build and test pipeline configured via GitHub Actions.

## ⚙️ Quick Start
1. Clone the repository: `git clone https://github.com/numele-tau/microservices-link-shortener.git`
2. Start the services: `docker compose up --build -d`
3. Access the API documentation (Swagger UI) at: `http://localhost/docs`