import logging
import os
from from_root import from_root
from datetime import datetime

# Log directory
LOG_DIR = "logs"
LOG_DIR_PATH = os.path.join(from_root(), LOG_DIR)

# Create logs directory (ONLY directory)
os.makedirs(LOG_DIR_PATH, exist_ok=True)

# Log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Full log file path
LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

