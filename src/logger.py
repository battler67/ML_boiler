import logging
import os

# Create only ONE logs folder
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Fixed log file name
LOG_FILE_PATH = os.path.join(logs_dir, "app.log")

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filemode="a"   # append mode (default, but good to be explicit)
)

# if __name__ == "__main__":
#     logging.info("Logging started")