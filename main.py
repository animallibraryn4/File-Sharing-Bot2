from bot import Bot
# In main.py or your bot start logic
from config import initialize_force_sub_channels

# Call it to populate FORCE_SUB_CHANNELS at the start
await initialize_force_sub_channels()
Bot().run()
