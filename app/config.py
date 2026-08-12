"""Application configuration management.

Settings are loaded from environment variables so that development,
staging, and production can be configured without code changes.
"""

import logging
import os

_DEFAULT_SECRET_KEY = "changeme-in-production"


class Config:
    """Base configuration."""

    APP_NAME: str = os.getenv("APP_NAME", "python-backend")
    ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    SECRET_KEY: str = os.getenv("SECRET_KEY", _DEFAULT_SECRET_KEY)


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = "DEBUG"


class StagingConfig(Config):
    DEBUG = False


class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = "WARNING"

    def __init__(self) -> None:
        super().__init__()
        if self.SECRET_KEY == _DEFAULT_SECRET_KEY:
            raise ValueError(
                "SECRET_KEY must be set to a strong random value in production. "
                "Never use the default key in a production environment."
            )


_ENV_CONFIG_MAP = {
    "development": DevelopmentConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}


def get_config() -> Config:
    """Return the correct Config class based on APP_ENV."""
    env = os.getenv("APP_ENV", "development")
    config_class = _ENV_CONFIG_MAP.get(env, DevelopmentConfig)
    return config_class()
