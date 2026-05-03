import logging
import os
import sys

# Create logs folder
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),      # save logs to file
        logging.StreamHandler(sys.stdout)   # show logs in console/notebook
    ]
)