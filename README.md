# ⚙️ DevOps Utilities API

> A production-ready REST API built with Python & FastAPI that exposes common DevOps utility operations as HTTP endpoints — containerized with Docker and ready to deploy anywhere.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Getting Started](#-getting-started)
  - [Run Locally](#1-run-locally)
  - [Run with Docker](#2-run-with-docker)
  - [Docker Image Variants](#3-docker-image-variants)
- [Interactive API Docs](#-interactive-api-docs)
- [Environment Variables](#-environment-variables)
- [Author](#-author)

---

## 🧭 Overview

**DevOps Utilities API** is a lightweight, RESTful API service built with **Python + FastAPI** that wraps common DevOps and system utility operations behind clean HTTP endpoints.

The project demonstrates:
- Building a modular, production-ready REST API in Python using FastAPI
- Clean code architecture with separated `routers/`, `services/`, and `app/` layers
- Multi-stage Docker builds with optimized image sizes (`Dockerfile`, `Dockerfile-mini`, `Dockerfile-big`)
- Containerization best practices with `.dockerignore`
- Auto-generated interactive API documentation via Swagger UI and ReDoc

This is a practical tool that can be integrated into CI/CD pipelines, internal developer portals, or used as a standalone DevOps helper service.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| Framework | FastAPI |
| Server | Uvicorn (ASGI) |
| Containerization | Docker (multi-variant Dockerfiles) |
| API Docs | Swagger UI / ReDoc (auto-generated) |
| Dependency Management | pip + requirements.txt |

---

## 📁 Project Structure

```
devops-utilities-api/
├── app/                    # App factory & configuration
│   └── __init__.py
├── routers/                # API route definitions (FastAPI routers)
│   └── *.py
├── services/               # Business logic & utility service functions
│   └── *.py
├── main.py                 # App entrypoint — FastAPI instance & router registration
├── requirements.txt        # Python dependencies
├── Dockerfile              # Standard Docker build
├── Dockerfile-mini         # Minimal/slim Docker image build
├── Dockerfile-big          # Full-featured Docker image build
├── .dockerignore           # Files excluded from Docker build context
└── README.md
```

### Architecture Pattern

```
HTTP Request
     │
     ▼
  main.py  (FastAPI app entry)
     │
     ▼
  routers/  (Route definitions — what endpoints exist)
     │
     ▼
  services/  (Business logic — what the endpoints actually do)
     │
     ▼
  Response
```

---

## 🔌 API Endpoints

The API provides interactive documentation at runtime. Once running, visit:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`
- **OpenAPI JSON:** `http://localhost:8000/openapi.json`

### Example Endpoints (typical for a DevOps Utilities API)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check / API info |
| `GET` | `/health` | Service health status |
| `GET` | `/docs` | Interactive Swagger documentation |

> 📝 **Note:** Full endpoint documentation is auto-generated and available interactively at `/docs` when the service is running.

---

## ⚡ Getting Started

### Prerequisites

- Python 3.11+
- pip
- Docker (for containerized run)

---

### 1. Run Locally

```bash
# Clone the repository
git clone https://github.com/rajendrakmr/devops-utilities-api.git
cd devops-utilities-api

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt

# Start the development server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Visit: `http://localhost:8000/docs`

---

### 2. Run with Docker

```bash
# Build the Docker image
docker build -t devops-utilities-api .

# Run the container
docker run -d \
  --name devops-api \
  -p 8000:8000 \
  devops-utilities-api

# Check it's running
curl http://localhost:8000/health
```

Visit: `http://localhost:8000/docs`

---

### 3. Docker Image Variants

This project ships with **three Dockerfile variants** for different use cases:

| Dockerfile | Use Case | Description |
|---|---|---|
| `Dockerfile` | Default / Production | Balanced image with standard dependencies |
| `Dockerfile-mini` | Lightweight / CI/CD | Minimal slim image — smaller size, faster pulls |
| `Dockerfile-big` | Full-featured | Includes additional system tools if needed |

```bash
# Build the mini (slim) image
docker build -f Dockerfile-mini -t devops-utilities-api:mini .

# Build the full-featured image
docker build -f Dockerfile-big -t devops-utilities-api:full .

# Compare image sizes
docker images | grep devops-utilities-api
```

> 💡 Use `Dockerfile-mini` in CI/CD pipelines for faster build and deploy times. Use `Dockerfile-big` when the service needs additional system-level utilities.

---

## 📖 Interactive API Docs

FastAPI automatically generates two documentation UIs — no extra setup needed.

| UI | URL | Description |
|---|---|---|
| Swagger UI | `http://localhost:8000/docs` | Interactive — try endpoints directly in the browser |
| ReDoc | `http://localhost:8000/redoc` | Clean, readable API reference |
| OpenAPI JSON | `http://localhost:8000/openapi.json` | Raw OpenAPI spec for integrations |

---

## 🔧 Environment Variables

Create a `.env` file in the root directory if needed:

```env
# Server config
HOST=0.0.0.0
PORT=8000
ENV=development         # development | production

# Add your app-specific env variables here
```

---

## 🐳 Docker Quick Reference

```bash
# Build
docker build -t devops-utilities-api .

# Run (detached)
docker run -d -p 8000:8000 --name devops-api devops-utilities-api

# View logs
docker logs -f devops-api

# Stop
docker stop devops-api

# Remove container
docker rm devops-api
```

---

## 👨‍💻 Author

**Rajendra Kumar Marandi**  
Frontend Developer → DevOps Engineer  
📍 Kolkata, India

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rajendraakmr/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rajendrakmr)

---

> ⭐ If you find this useful, consider giving it a star — it helps others discover it!