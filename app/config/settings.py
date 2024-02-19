"""Base setting for the application."""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Get Settings from env file or env variables"""

    PROJECT_NAME: str = "Call Center Sim"
    PROJECT_VERSION: str = "0.0.1"
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=("example.env", ".env", "dev.env", "prod.env"), extra="ignore"
    )


settings = Settings()


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Get settings from env file or env variables"""
    return Settings()
