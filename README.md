# Python Docker Application

A containerized Python web application built with Docker, designed for local development and production deployment on AWS. This project follows a feature-branch workflow to separate concerns across setup, containerization, API development, database integration, CI/CD, and cloud deployment.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Branching Strategy](#branching-strategy)
4. [Project Structure](#project-structure)
5. [Prerequisites](#prerequisites)
6. [Local Development](#local-development)
7. [Docker Setup](#docker-setup)
8. [API Development](#api-development)
9. [Database](#database)
10. [CI/CD](#cicd)
11. [AWS Deployment](#aws-deployment)
12. [Environment Variables](#environment-variables)
13. [Contributing](#contributing)
14. [License](#license)

---

## Project Overview

This repository contains the source code and configuration for a Python-based application packaged as a Docker image. The goal is to provide a clean, scalable foundation that can be built locally, tested automatically, and deployed to AWS infrastructure.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.x |
| Web Framework | Flask / FastAPI (TBD) |
| Containerization | Docker|
| Database | PostgreSQL  |
| CI/CD | GitHub Actions / Jenkins |
| Cloud Platform | AWS (ECS / ECR / EC2 / Elastic Beanstalk) |
| Orchestration | AWS ECS Fargate (recommended) |

---

## Branching Strategy

Development is organized into focused feature branches. Each branch isolates a specific phase or concern of the project. Merge requests should target `main` after review and successful CI checks.

```
main
 │
 ├── feature/project-setup
 ├── feature/docker-setup
 ├── feature/api-development
 ├── feature/database
 ├── feature/ci-cd
 └── feature/aws-deployment
```

### Branch Descriptions

| Branch | Purpose |
|--------|---------|
| `main` | Production-ready source of truth. |
| `feature/project-setup` | Initial project scaffolding, dependency management, and tooling configuration. |
| `feature/docker-setup` | Dockerfile, `.dockerignore`, and Docker Compose configuration. |
| `feature/api-development` | REST API routes, controllers, services, and business logic. |
| `feature/database` | Database models, migrations, connection handling, and seed data. |
| `feature/ci-cd` | Continuous integration and delivery pipelines. |
| `feature/aws-deployment` | AWS infrastructure configuration, deployment scripts, and environment provisioning. |

---

## Project Structure

```
python-docker-project/
├── .github/
│   └── workflows/              # CI/CD pipeline definitions
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── api/                    # API routes and controllers
│   ├── core/                   # Configuration and shared utilities
│   ├── db/                     # Database models and migrations
│   └── services/               # Business logic
├── infra/
│   ├── aws/                    # AWS CloudFormation / Terraform / ECS task definitions
│   └── docker/                 # Docker-related assets
├── tests/
│   ├── unit/                   # Unit tests
│   └── integration/            # Integration tests
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.10+
- Docker Desktop
- Docker Compose
- Git
- AWS CLI (for deployment)
- (Optional) Terraform or AWS CloudFormation CLI

---

## Local Development

### 1. Clone the Repository

```bash
git clone <repository-url>
cd python-docker-project
```

### 2. Create and Activate a Virtual Environment

#### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> If activation fails with an execution-policy error, run PowerShell as Administrator and execute:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

#### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your local settings.

### 4. Run the Application Locally

```bash
python app/main.py
```

---

## Docker Setup

### Build the Docker Image

```bash
docker build -t python-docker-app .
```

### Run the Container

```bash
docker run -p 8000:8000 --env-file .env python-docker-app
```

### Run with Docker Compose

```bash
docker-compose up --build
```

### Stop Services

```bash
docker-compose down
```

---

## API Development

- API routes live under `app/api/`.
- Use Pydantic models for request/response validation when using FastAPI.
- Keep business logic in `app/services/`.
- Add tests for every new endpoint under `tests/`.

### Example Endpoint

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

## Database

- Database configuration is managed under `app/db/`.
- Use Alembic or Flask-Migrate for schema migrations.
- Connection strings should be read from environment variables.

### Run Migrations

```bash
alembic upgrade head
```

---

## CI/CD

The CI/CD pipeline is defined in `.github/workflows/` or an equivalent Jenkinsfile. It typically includes:

1. Code checkout
2. Dependency installation
3. Linting and formatting checks
4. Unit and integration tests
5. Docker image build
6. Image push to Amazon ECR
7. Deployment to AWS (ECS / Elastic Beanstalk / EC2)

### Triggering a Deployment

Merging a pull request into `main` triggers the deployment pipeline automatically.

---

## AWS Deployment

### Deployment Options

| Service | Use Case |
|---------|----------|
| Amazon ECR | Store Docker images |
| Amazon ECS (Fargate) | Serverless container orchestration |
| AWS Elastic Beanstalk | Simple managed application deployment |
| Amazon EC2 | Full control over compute instances |

### Deployment Steps

1. Build and tag the Docker image:

```bash
docker build -t python-docker-app .
```

2. Authenticate with Amazon ECR:

```bash
aws ecr get-login-password --region <region> | \
  docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
```

3. Tag and push the image:

```bash
docker tag python-docker-app:latest <account-id>.dkr.ecr.<region>.amazonaws.com/python-docker-app:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/python-docker-app:latest
```

4. Update the ECS service or Elastic Beanstalk environment to use the new image.

### Infrastructure as Code

AWS resources can be provisioned using:

- AWS CloudFormation templates in `infra/aws/cloudformation/`
- Terraform configurations in `infra/aws/terraform/`

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```env
APP_NAME=python-docker-app
APP_ENV=development
DEBUG=true
HOST=0.0.0.0
PORT=8000
DATABASE_URL=postgresql://user:password@db:5432/appdb
AWS_REGION=us-east-1
AWS_ECR_REPOSITORY=python-docker-app
AWS_ECS_CLUSTER=python-docker-cluster
AWS_ECS_SERVICE=python-docker-service
```

---

## Contributing

1. Create a feature branch from `main`:

```bash
git checkout -b feature/<branch-name>
```

2. Make your changes and commit them with clear messages.
3. Push the branch and open a pull request to `main`.
4. Ensure all CI checks pass before merging.

### Commit Message Convention

```
feat: add health check endpoint
fix: resolve database connection timeout
docs: update README with deployment steps
chore: update dependencies
```

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.