
# ACEest Fitness & Gym — DevOps Assignment Starter

A minimal Flask API that mirrors basic ACEest Fitness functionality (add workout, list workouts), with Pytest tests, Dockerfile, and a GitHub Actions CI pipeline.

## Endpoints
- `GET /health` → health check
- `GET /workouts` → list all workouts
- `POST /workouts` → add a workout using JSON body: `{"workout": "Running", "duration": 30}`

## Run locally

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
python app.py
# App runs on http://127.0.0.1:5000
```

## Run tests locally

```bash
pytest -q
```

## Build & run with Docker

```bash
docker build -t aceest-fitness .
docker run --rm -p 5000:5000 aceest-fitness
# Open http://127.0.0.1:5000/health
```

## GitHub Actions CI

- Runs Pytest on push and PR
- Builds the Docker image
- Runs tests **inside** the Docker image as well

See `.github/workflows/ci.yml`.
