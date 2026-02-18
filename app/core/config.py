import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Water Quality AI Backend"
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:postgres@db:5432/waterdb"
    )
    MODEL_PATH: str = os.getenv("MODEL_PATH", "app/ml/models/water_model_v1.pkl")
    MODEL_VERSION: str = os.getenv("MODEL_VERSION", "v1")

    class Config:
        env_file = ".env"


settings = Settings()
