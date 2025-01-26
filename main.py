from dotenv import load_dotenv
load_dotenv()
import os

required_env_vars = ["BOT_TOKEN", "API_ID", "API_HASH", "OWNER_ID", "DB_URL", "DB_NAME", "CHANNEL_ID"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
else:
    print("All required environment variables are set.")
  
from config import initialize_force_sub_channels, fetch_force_sub_channels

# Initialize the channels at the start
initialize_force_sub_channels()

# Example usage
print("Current FORCE_SUB_CHANNELS:", fetch_force_sub_channels())

import time

def main():
    print("Application is running...")
    while True:
        time.sleep(10)  # Keeps the app running

if __name__ == "__main__":
    main()
