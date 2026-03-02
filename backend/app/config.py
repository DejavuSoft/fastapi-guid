from pydantic_settings import BaseSettings
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent.parent

class Setting(BaseSettings):
    app_name: str = "ServerBase API"
    debug: bool = True
    database_url: str = f"sqlite:///{BACKEND_DIR}/guid.db"
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ]
    static_dir: str = f"{BACKEND_DIR}/static"
    images_dir: str = f"{BACKEND_DIR}/static/images"

    class Config:
        env_file = ".env"

settings = Setting()