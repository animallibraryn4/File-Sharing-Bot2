import os
import logging
from logging.handlers import RotatingFileHandler
from channel_manager import fetch_force_sub_channels  # Importing from channel_manager

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7838121435:AAHcr9fXepUu0DlojD0YFvDHzubAPHAQ_7I")
API_ID = int(os.environ.get("API_ID", "22299340"))
API_HASH = os.environ.get("API_HASH", "09b09f3e2ff1306da4a19888f614d937")

OWNER_ID = int(os.environ.get("OWNER_ID", "5380609667"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://n4animeedit:u80hdwhlka5NBFfY@cluster0.jowvb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "n4animeedit")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002263636517"))

# config.py
FORCE_SUB_CHANNELS = ["@channel1", "@channel2", "@channel3"]

PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Admins list from environment variable
try:
    ADMINS = [5380609667]
    for x in (os.environ.get("ADMINS", "5380609667").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Other config options...
FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600"))  # auto delete in minutes

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
