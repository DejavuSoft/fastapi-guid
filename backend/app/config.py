from pydantic_settings import BaseSettings
from pathlib import Path

def get_local_ip():
    import socket
    try:
        # Создаём временный UDP-сокет и "подключаемся" к внешнему адресу
        # (данные не отправляются, но система сообщает, какой IP будет использоваться)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))          # можно использовать 1.1.1.1, 208.67.222.222 и т.д.
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None

LOCAL_IP = get_local_ip()
BACKEND_DIR = Path(__file__).resolve().parent.parent

class Setting(BaseSettings):
    app_name: str = "ServerBase API"
    debug: bool = True
    database_url: str = f"sqlite:///{BACKEND_DIR}/guid.db"
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        f"http://{LOCAL_IP}:3000",
        f"http://{LOCAL_IP}:5173"
    ]
    static_dir: str = f"{BACKEND_DIR}/static"
    images_dir: str = f"{BACKEND_DIR}/static/images"

    class Config:
        env_file = ".env"

settings = Setting()