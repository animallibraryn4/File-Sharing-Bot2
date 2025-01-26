import os
import time
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

required_env_vars = ["BOT_TOKEN", "API_ID", "API_HASH", "OWNER_ID", "DB_URL", "DB_NAME", "CHANNEL_ID"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
else:
    logging.info("All required environment variables are set.")

from config import initialize_force_sub_channels, fetch_force_sub_channels

# Initialize the channels at the start
initialize_force_sub_channels()

# Example usage
logging.info(f"Current FORCE_SUB_CHANNELS: {fetch_force_sub_channels()}")

def main():
    logging.info("Application is running...")
    while True:
        time.sleep(10)  # Keeps the app running

if __name__ == "__main__":
    main()
