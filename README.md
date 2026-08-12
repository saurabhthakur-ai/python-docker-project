# python-docker-project

A production-ready Python backend starter built with Flask, packaged with Docker, and wired for GitHub Actions CI/CD.

---

## Project structure

```
.
├── app/
│   ├── __init__.py
│   ├── config.py      # Environment-based configuration
│   ├── logger.py      # Centralised logging setup
│   └── main.py        # Flask app factory + routes
├── tests/
│   └── test_health.py
├── .env.example       # Copy to .env – never commit .env
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml     # GitHub Actions CI pipeline
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

---

## Quick start (local)

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional but recommended)

### 1 – Clone and set up a virtual environment

```bash
git clone https://github.com/saurabhthakur-ai/python-docker-project.git
cd python-docker-project
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt
```

### 2 – Configure environment variables

```bash
cp .env.example .env
# Edit .env and fill in real values (especially SECRET_KEY in production)
```

### 3 – Run locally

```bash
python -m app.main
# App listens on http://localhost:8000
```

---

## Testing

```bash
pytest tests/ --tb=short --cov=app --cov-report=term-missing
```

---

## Docker

### Build and run with Docker Compose (recommended for development)

```bash
docker compose up --build
```

### Build and run with plain Docker

```bash
docker build -t python-backend .
docker run --env-file .env -p 8000:8000 python-backend
```

### Health check

```
GET http://localhost:8000/health
```

Response:

```json
{
  "status": "ok",
  "environment": "development",
  "uptime_seconds": 12.34,
  "python": "3.12.x"
}
```

---

## Configuration

All configuration is driven by environment variables (see `.env.example`).

| Variable    | Default          | Description                          |
|-------------|------------------|--------------------------------------|
| `APP_NAME`  | `python-backend` | Application name                     |
| `APP_ENV`   | `development`    | `development` / `staging` / `production` |
| `DEBUG`     | `false`          | Enable Flask debug mode              |
| `HOST`      | `0.0.0.0`        | Bind host                            |
| `PORT`      | `8000`           | Bind port                            |
| `LOG_LEVEL` | `INFO`           | Log level (`DEBUG`, `INFO`, `WARNING`, `ERROR`) |
| `SECRET_KEY`| *(changeme)*     | Flask secret key – set a strong value in production |

---

## CI/CD (GitHub Actions)

The `.github/workflows/ci.yml` pipeline:

1. Runs on every push to `main` or `feature/**` branches and on PRs targeting `main`.
2. Installs dependencies and runs the test suite with coverage.
3. Builds the Docker image to catch build regressions.

### Deploying to AWS

The Docker image produced by this project is compatible with:

- **AWS ECS / Fargate** – push the image to ECR and deploy a Fargate task.
- **AWS App Runner** – connect your ECR repository for zero-config deployment.
- **AWS Elastic Beanstalk** – use the multi-container Docker platform.

Set `APP_ENV=production` and provide a strong `SECRET_KEY` via AWS Secrets Manager or Parameter Store.

---

## Git workflow

This project follows an enterprise feature-branch workflow:

1. Create a branch: `git checkout -b feature/<short-description>`
2. Commit and push your changes.
3. Open a Pull Request targeting `main`.
4. Merge only after CI passes and at least one review approval.

---

## Security notes

- Secrets are never committed – `.env` is in `.gitignore`.
- The production Docker image runs as a non-root user.
- Rotate `SECRET_KEY` regularly and use a secrets manager in production.
