from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>🤖 My Name :</b> <a href='https://t.me/FileSharingXProBot'>File Sharing Bot</a> \n<b>📝 Language :</b> <a href='https://python.org'>Python 3</a> \n<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram {__version__}</a> \n<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a> \n<b>📢 Channel :</b> <a href='https://t.me/+xgkHNeh4_qg1Y2Jl'>Anime library N4</a> \n<b>🧑‍💻 Developer :</b> <a href='tg://5380609667={OWNER_ID}'>Eren</a>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ],
                    [
                        InlineKeyboardButton("💬 CUSTOM CAPTION", callback_data="custom_caption"),
                        InlineKeyboardButton("🚀 CUSTOM FORCE SUBSCRIBE", callback_data="custom_force_subscribe")
                    ],
                    [
                        InlineKeyboardButton("🔘 CUSTOM BUTTON", callback_data="custom_button")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "custom_caption":
        await query.message.edit_text("This is the custom caption.")
    elif data == "custom_force_subscribe":
        await query.message.edit_text("Please subscribe to the channel to continue.")
    elif data == "custom_button":
        await query.message.edit_text("You clicked the custom button!")
