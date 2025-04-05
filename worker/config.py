import os
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
import pathlib
from pathlib import Path



class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USER: str
    REDIS_PASSWORD: str
    
    RABBIT_HOST: str
    RABBIT_PORT: int
    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str
    
    FILE_TEMP_DIR: Path
    BASE_DIR: Path  = Path.cwd()
    
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR.parent}/.env",
        extra="ignore"
        )
    
    @field_validator("FILE_TEMP_DIR", mode="before")
    @classmethod
    def create_file_temp(cls, value: str):
        result = Path(value)
        result.mkdir(parents=True, exist_ok=True)
        return result.absolute()
        

settings = Settings()

os.environ["BASE_DIR"] = str(settings.BASE_DIR)
