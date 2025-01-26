import pymongo, os
from config import DB_URL, DB_NAME

dbclient = pymongo.MongoClient(DB_URL)
database = dbclient[DB_NAME]
user_data = database['users']

async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

import pymongo, os
from config import DB_URL, DB_NAME

dbclient = pymongo.MongoClient(DB_URL)
database = dbclient[DB_NAME]

# User collection
user_data = database['users']

# Channel collection for FORCE_SUB_CHANNEL values
channel_data = database['channels']

# Function to check if a user is present in the database
async def present_user(user_id: int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

# Function to add a user to the database
async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

# Function to get all user IDs in the database
async def full_userbase():
    user_docs = user_data.find()
    user_ids = [doc['_id'] for doc in user_docs]
    return user_ids

# Function to delete a user from the database
async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

# Function to get all FORCE_SUB_CHANNEL values
async def get_force_sub_channels():
    channels = channel_data.find()
    channel_ids = [channel['channel_id'] for channel in channels]
    return channel_ids

# Function to add a new FORCE_SUB_CHANNEL
async def add_force_sub_channel(channel_id: int):
    # Check if the channel already exists
    existing_channel = channel_data.find_one({'channel_id': channel_id})
    if not existing_channel:
        channel_data.insert_one({'channel_id': channel_id})
    return

# Function to delete a FORCE_SUB_CHANNEL
async def del_force_sub_channel(channel_id: int):
    channel_data.delete_one({'channel_id': channel_id})
    return

# Function to update an existing FORCE_SUB_CHANNEL (if required)
async def update_force_sub_channel(old_channel_id: int, new_channel_id: int):
    channel_data.update_one(
        {'channel_id': old_channel_id},
        {'$set': {'channel_id': new_channel_id}}
    )
    return








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
