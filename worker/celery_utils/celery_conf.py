from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

from config import settings


class CelerySettings(BaseSettings):
    broker_url: str = f"pyamqp://{settings.RABBITMQ_DEFAULT_USER}:{settings.RABBITMQ_DEFAULT_PASS}@{settings.RABBIT_HOST}:{settings.RABBIT_PORT}//"
    result_backend: str = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/0"
    # task_serializer: str = "json"
    # result_serializer: str = "json"
    # accept_content: list[str] = ["json"]
    timezone: str = Field(alias="TZ")
    enable_utc: bool = False
    task_routes: dict = {}

    # В env обязательно должен быть указан корень проекта, где лежит 
    # env файл
    model_config = SettingsConfigDict(
        env_file=f"{Path(os.getenv("BASE_DIR"))}/.env",
        extra="ignore"
        )