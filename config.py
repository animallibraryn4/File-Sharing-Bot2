import os
import logging
from logging.handlers import RotatingFileHandler

# Initialize the list of force subscription channels with default values
FORCE_SUB_CHANNELS = ["@default_channel1", "@default_channel2", "@default_channel3"]

# Configure logging
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

# Function to get a logger instance
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Function to dynamically update the force subscription channels
def update_force_sub_channels(new_channels):
    """
    Dynamically update the list of force subscription channels.
    new_channels should be a list of exactly 3 channels.
    """
    global FORCE_SUB_CHANNELS
    
    if len(new_channels) == 3:
        FORCE_SUB_CHANNELS = new_channels
        logging.info(f"Updated FORCE_SUB_CHANNELS to: {FORCE_SUB_CHANNELS}")
    else:
        logging.error("You must provide exactly 3 channels.")

# Function to initialize the force subscription channels (default values or dynamically)
def initialize_force_sub_channels():
    """
    Initialize the FORCE_SUB_CHANNELS with default values or from an external source.
    """
    global FORCE_SUB_CHANNELS
    
    # Example: Load channels from a file if it exists, otherwise use default
    file_path = "settings.txt"
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                channels = file.read().splitlines()
                if len(channels) == 3:
                    FORCE_SUB_CHANNELS = channels
                    LOGGER(__name__).info(f"Initialized FORCE_SUB_CHANNELS from file: {FORCE_SUB_CHANNELS}")
                else:
                    LOGGER(__name__).error("Settings file must contain exactly 3 channels.")
        except Exception as e:
            LOGGER(__name__).error(f"Error initializing FORCE_SUB_CHANNELS from file: {e}")
    else:
        LOGGER(__name__).info("Using default FORCE_SUB_CHANNELS.")

# Example method to fetch the current force subscription channels
def fetch_force_sub_channels():
    """
    Fetch the current list of force subscription channels.
    """
    return FORCE_SUB_CHANNELS

# Configuration constants from environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7838121435:AAHcr9fXepUu0DlojD0YFvDHzubAPHAQ_7I")
API_ID = int(os.environ.get("API_ID", "22299340"))
API_HASH = os.environ.get("API_HASH", "09b09f3e2ff1306da4a19888f614d937")
OWNER_ID = int(os.environ.get("OWNER_ID", "5380609667"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://n4animeedit:u80hdwhlka5NBFfY@cluster0.jowvb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "n4animeedit")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002263636517"))

# Set up other configuration options
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
