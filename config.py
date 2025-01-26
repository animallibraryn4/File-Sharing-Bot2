import os
import logging
from logging.handlers import RotatingFileHandler
from config import fetch_force_sub_channels


# On bot start
async def on_start():
    await fetch_force_sub_channels()  # Fetch the channels from DB and initialize FORCE_SUB_CHANNELS



BOT_TOKEN = os.environ.get("BOT_TOKEN", "7838121435:AAHcr9fXepUu0DlojD0YFvDHzubAPHAQ_7I")
API_ID = int(os.environ.get("API_ID", "22299340"))
API_HASH = os.environ.get("API_HASH", "09b09f3e2ff1306da4a19888f614d937")


OWNER_ID = int(os.environ.get("OWNER_ID", "5380609667"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://n4animeedit:u80hdwhlka5NBFfY@cluster0.jowvb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "n4animeedit")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002263636517"))

from pyrogram import Client, filters
from config import ADMINS
from database import add_force_sub_channel, del_force_sub_channel, get_force_sub_channels

@app.on_message(filters.command("addchannel") & filters.user(ADMINS))  # Only admins can add channels
async def add_channel(client, message):
    try:
        new_channel = message.text.split()[1]  # Extract the new channel ID
        await add_force_sub_channel(new_channel)  # Add the channel to the database
        await message.reply(f"New Force Sub Channel {new_channel} has been added!")
    except IndexError:
        await message.reply("Please provide the channel ID to add.")
    except Exception as e:
        await message.reply(f"Error: {str(e)}")

@app.on_message(filters.command("delchannel") & filters.user(ADMINS))  # Only admins can remove channels
async def del_channel(client, message):
    try:
        channel_to_remove = message.text.split()[1]  # Extract the channel ID
        await del_force_sub_channel(channel_to_remove)  # Remove the channel from the database
        await message.reply(f"Force Sub Channel {channel_to_remove} has been removed!")
    except IndexError:
        await message.reply("Please provide the channel ID to remove.")
    except Exception as e:
        await message.reply(f"Error: {str(e)}")

@app.on_message(filters.command("listchannels") & filters.user(ADMINS))  # Only admins can list channels
async def list_channels(client, message):
    channels = await get_force_sub_channels()  # Get all channels from the database
    if channels:
        channels_list = "\n".join(channels)
        await message.reply(f"Current Force Sub Channels:\n{channels_list}")
    else:
        await message.reply("No Force Sub Channels found.")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in minute


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[5380609667]
    for x in (os.environ.get("ADMINS", "5380609667").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "📀")

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel To Use Me\n\nKindly Please Join Channel</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(5380609667)

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
   





