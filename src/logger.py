import logging
import os
from datetime import datetime

# Create logs directory path and log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Create complete log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging with proper level and format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Set the logging level to INFO
    filemode='w'  # 'w' mode overwrites the file, 'a' would append
)

# Create a logger instance
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        logger.info("Logging has started")
        # Add some test logs
        #logger.debug("This is a debug message")
        #logger.info("This is an info message")
        #logger.warning("This is a warning message")
        #logger.error("This is an error message")
    except Exception as e:
        logger.exception("An error occurred while logging")