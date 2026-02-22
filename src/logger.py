import logging
import os
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]  # src/ → project root

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = PROJECT_ROOT / "logs" / LOG_FILE
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = logs_path / LOG_FILE 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

