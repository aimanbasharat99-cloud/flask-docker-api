# Dockerised Flask REST API

> A containerised REST API built with Flask and Docker — serving image processing and datetime endpoints.

Built as **Assignment 3 for Software Integration II during my MSc in International Biometrics and Intelligent Vision at UPEC, Paris.**

---

## What It Does

A lightweight Flask API with two endpoints:
- **GET `/datetime`** — returns the current server date and time
- **POST `/flip`** — accepts an image and returns it horizontally flipped

The entire app is containerised with **Docker**, meaning anyone can run it instantly with a single command — no setup needed.

---

## How It Works

```
User sends request
       ↓
Docker container runs Flask app on port 5000
       ↓
/datetime → returns current timestamp as JSON
/flip     → receives image → flips it → returns flipped image
       ↓
test_api.py verifies both endpoints automatically
```

---

## Features

- **Fully Dockerised** — runs anywhere with one command
- **REST API** — clean endpoints, easy to integrate
- **Image processing** — horizontal flip via Pillow
- **Automated tests** — `test_api.py` tests both endpoints
- **Lightweight** — only Flask and Pillow as dependencies

---

## Tech Stack

| Layer | Technology |
|---|---|
| API | Flask |
| Image Processing | Pillow |
| Containerisation | Docker |
| Testing | Python requests |

---

## How to Run

**Option A — With Docker (recommended)**

```bash
docker build -t flask-api .
docker run -p 5000:5000 flask-api
```

API is now live at `http://localhost:5000`

**Option B — Without Docker**

```bash
pip install -r requirements.txt
python app.py
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/datetime` | Returns current datetime |
| POST | `/flip` | Flips uploaded image horizontally |

**Test the datetime endpoint:**
```bash
curl http://localhost:5000/datetime
```

Response:
```json
{
  "datetime": "2026-05-31 14:32:10.123456"
}
```

**Test the flip endpoint:**
```bash
curl -X POST -F "image=@test.jpg" http://localhost:5000/flip --output flipped.jpg
```

---

## Run Automated Tests

```bash
python test_api.py
```

This tests both endpoints and saves the flipped image as `flipped.jpg`.

---

## Project Structure

```
flask-docker-api/
├── app.py            # Flask application
├── Dockerfile        # Docker configuration
├── requirements.txt  # Dependencies
├── test_api.py       # Automated API tests
└── test.jpg          # Sample test image
```

---

## Author

**Aiman Basharat Abbasi**
MSc — International Biometrics & Intelligent Vision, UPEC Paris
[LinkedIn](https://linkedin.com/in/aiman-basharat-abbasi-892137219) · [GitHub](https://github.com/aimanbasharat99-cloud)
