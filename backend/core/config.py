from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    SERVER_HOST: str
    SERVER_PORT: int
    ENV: str
    SQLITE_DB_PATH: str
    BASE_URL: str
    SHORT_CODE_LENGTH: int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

# SQLite连接串
SQLALCHEMY_DATABASE_URL = f"sqlite:///{settings.SQLITE_DB_PATH}"