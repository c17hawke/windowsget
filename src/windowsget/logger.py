"""
Logger module for logging
"""
import os
import logging
import sys

LOGGING_STR = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
LOG_DIR = "./logs"
log_filepath = os.path.join(LOG_DIR, "running_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=LOGGING_STR,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("windowsget")
