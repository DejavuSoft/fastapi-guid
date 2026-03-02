import uvicorn
import subprocess
from app.config import settings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

if __name__ == "__main__":
    subprocess.Popen(["npm", "run", "dev"], cwd=str(FRONTEND_DIR), shell=True)
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level='info'
    )