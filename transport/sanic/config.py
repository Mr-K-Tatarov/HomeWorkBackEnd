import os

from dotenv import load_dotenv

load_dotenv()


class SanicConfig:
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("POST", 8000))
    workers = int(os.getenv("WORKERS", 1))
    debug = bool(os.getenv("DEBUG", False))
