import os
from config import LOGGER

# Function to fetch force subscription channels from a file (or any other external source like DB)
def fetch_force_sub_channels():
    try:
        # For example, reading from settings.txt where the channel name is stored
        with open("settings.txt", "r") as file:
            channels = file.read().splitlines()
            LOGGER(__name__).info(f"Fetched Force Sub Channels: {channels}")
            return channels
    except Exception as e:
        LOGGER(__name__).error(f"Error fetching force sub channels: {e}")
        return []

# Function to update the list of force subscription channels (writes to a file or database)
def update_force_sub_channels(channels):
    try:
        with open("settings.txt", "w") as file:
            # Writing each channel on a new line
            file.writelines([f"{channel}\n" for channel in channels])
            LOGGER(__name__).info(f"Force Sub Channels updated: {channels}")
    except Exception as e:
        LOGGER(__name__).error(f"Error updating force sub channels: {e}")
