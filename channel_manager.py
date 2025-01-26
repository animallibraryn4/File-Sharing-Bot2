import os

# Function to fetch force subscription channels from a file
def fetch_force_sub_channels():
    try:
        with open("settings.txt", "r") as file:
            channels = file.read().splitlines()
            log_info(f"Fetched Force Sub Channels: {channels}")
            return channels
    except Exception as e:
        log_error(f"Error fetching force sub channels: {e}")
        return []

# Function to update the list of force subscription channels
def update_force_sub_channels(channels):
    try:
        with open("settings.txt", "w") as file:
            file.writelines([f"{channel}\n" for channel in channels])
            log_info(f"Force Sub Channels updated: {channels}")
    except Exception as e:
        log_error(f"Error updating force sub channels: {e}")

# Helper functions to handle logging
def log_info(message):
    from config import LOGGER  # Import here to avoid circular dependency
    LOGGER(__name__).info(message)

def log_error(message):
    from config import LOGGER  # Import here to avoid circular dependency
    LOGGER(__name__).error(message)

# Function to add new channels
def add_new_channel(channel):
    channels = fetch_force_sub_channels()
    if channel not in channels:
        channels.append(channel)
        update_force_sub_channels(channels)
        log_info(f"Added new channel: {channel}")
    else:
        log_info(f"Channel {channel} already exists in the list.")
