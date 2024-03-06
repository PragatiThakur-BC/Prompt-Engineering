from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
    """
    Setting class for the application
    """
    TOGETHER_API_KEY: str
    BASE_URL: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    MODEL: str
    MAX_TOKENS: int
    GPT_API_KEY: str
    GPT_MODEL: str

    class Config:
        env_file = ".env"


settings = Settings()
