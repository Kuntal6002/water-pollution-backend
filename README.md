# 🌊 Water Pollution Detection Backend (AI-Ready)

A production-structured **FastAPI backend** for real-time water quality
monitoring and AI-based pollution classification.

------------------------------------------------------------------------

## 📌 Overview

This system:

-   Accepts water sensor readings via API\
-   Validates input ranges\
-   Stores readings in PostgreSQL\
-   Integrates with a pluggable ML inference layer\
-   Supports real-time streaming via WebSocket\
-   Runs fully containerized using Docker

------------------------------------------------------------------------

# 🏗 Architecture Overview

    Frontend / Sensors
            |
            v
        FastAPI API Layer
            |
      ---------------------
      |         |         |
    PostgreSQL  ML Layer  WebSocket

------------------------------------------------------------------------

## 🧠 Key Design Principles

-   Clean separation of concerns\
-   ML adapter layer (easily replaceable)\
-   Dockerized infrastructure\
-   Production-ready structure\
-   Input validation with Pydantic\
-   ORM-based persistence (SQLAlchemy)

------------------------------------------------------------------------

# 📁 Project Structure

    app/
    ├── api/                # HTTP & WebSocket routes
    ├── core/               # Config & logging
    ├── db/                 # Database models & session
    ├── schemas/            # Pydantic schemas
    ├── services/           # Business & inference logic
    ├── ml/                 # Future ML models
    ├── dependencies.py     # Dependency Injection layer
    └── main.py

------------------------------------------------------------------------

# 🚀 Features

## 1️⃣ Ingest Water Readings

**POST `/ingest`**

### Request

``` json
{
  "ph": 7.2,
  "turbidity": 3.5,
  "tds": 200,
  "temperature": 25,
  "dissolved_oxygen": 6
}
```

### Response

``` json
{
  "prediction": "Safe",
  "confidence": 0.87
}
```

------------------------------------------------------------------------

## 2️⃣ Get Latest Reading

**GET `/latest`**

Returns the most recent reading along with prediction and confidence.

------------------------------------------------------------------------

## 3️⃣ Get Historical Data

**GET `/history?skip=0&limit=10`**

Returns paginated historical readings.

------------------------------------------------------------------------

## 4️⃣ Real-Time Stream

**WebSocket `/stream`**

Streams newly added readings and predictions in real time.

------------------------------------------------------------------------

# 🤖 ML Integration Design

The system includes an `InferenceService` that:

-   Loads model if available using `joblib.load`
-   Falls back to mock predictions if model is not present
-   Supports model versioning
-   Easily replaceable with:
    -   Remote ML microservice
    -   TensorFlow / PyTorch model
    -   Batch inference system

### Example Future Integration

``` python
joblib.load("app/ml/models/water_model_v1.pkl")
```

No changes required in the API layer.

------------------------------------------------------------------------

# 🐳 Docker Setup

## 📦 Prerequisites

-   Docker\
-   Docker Compose

------------------------------------------------------------------------

## 🔧 Build & Run

``` bash
docker-compose build
docker-compose up
```

Backend will be available at:

    http://localhost:8000

------------------------------------------------------------------------

# 🧪 Testing the API

## Ingest Data

``` bash
curl -X POST http://localhost:8000/ingest -H "Content-Type: application/json" -d '{
  "ph": 7.2,
  "turbidity": 3.5,
  "tds": 200,
  "temperature": 25,
  "dissolved_oxygen": 6
}'
```

## Get Latest Reading

``` bash
curl http://localhost:8000/latest
```

## Get History

``` bash
curl "http://localhost:8000/history?skip=0&limit=5"
```

------------------------------------------------------------------------

# 🛢 Database

-   PostgreSQL 15\
-   SQLAlchemy ORM\
-   Containerized setup\
-   Persistent volume via Docker

### Connect Manually (if exposed to host)

``` bash
psql -h localhost -p 5433 -U postgres -d waterdb
```

------------------------------------------------------------------------

# 🔐 Input Validation Rules

  Parameter          Rule
  ------------------ ------------
  pH                 0--14
  Turbidity          ≥ 0
  TDS                ≥ 0
  Temperature        -10 to 100
  Dissolved Oxygen   ≥ 0

Invalid input returns:

    422 Unprocessable Entity

------------------------------------------------------------------------

# 🧠 Why This Architecture?

This project is structured to:

-   Allow ML team to plug in models without backend refactor\
-   Support scaling to physical sensor hardware later\
-   Enable dashboard frontend integration\
-   Maintain prediction audit history\
-   Evolve into a production-grade microservice

------------------------------------------------------------------------

# 🔮 Future Improvements

-   Async SQLAlchemy\
-   Redis pub/sub for real-time broadcast\
-   JWT authentication\
-   Alembic migrations\
-   Background task queue (Celery / RQ)\
-   Alerting system for high pollution events\
-   Dashboard frontend

------------------------------------------------------------------------

# 📦 Tech Stack

-   FastAPI\
-   PostgreSQL\
-   SQLAlchemy\
-   Pydantic v2\
-   Docker\
-   Joblib

------------------------------------------------------------------------

# 👨‍💻 Development Mode (Without Docker)

``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
