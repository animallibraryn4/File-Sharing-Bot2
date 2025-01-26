from bot import Bot
import asyncio
from config import initialize_force_sub_channels
from bot import Bot  # Assuming your Bot class is in bot.py

async def main():
    # Initialize force subscription channels
    await initialize_force_sub_channels()

    # Start your bot here (this depends on how your bot is structured)
    bot = Bot()  # Example, replace it with your bot initialization
    await bot.run()  # Assuming your bot has a `run()` method to start the bot

# Run the main async function
if __name__ == "__main__":
    asyncio.run(main())  # This ensures that the async function is run correctly
