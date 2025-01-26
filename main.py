from config import initialize_force_sub_channels, fetch_force_sub_channels

# Initialize the channels at the start
initialize_force_sub_channels()

# Example usage
print("Current FORCE_SUB_CHANNELS:", fetch_force_sub_channels())
