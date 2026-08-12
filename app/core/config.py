"""Application configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = "python-docker-app"
    app_env: str = "development"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    database_url: str = "postgresql://user:password@db:5432/appdb"
    aws_region: str = "us-east-1"
    aws_ecr_repository: str = "python-docker-app"
    aws_ecs_cluster: str = "python-docker-cluster"
    aws_ecs_service: str = "python-docker-service"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
