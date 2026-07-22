"""
Purpose:
Manage all application configuration from environment variables.

Used By:
Entire MindRankAI backend.

Edit Carefully:
Only configuration should be placed here.
Do not write business logic in this file.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "MindRankAI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()