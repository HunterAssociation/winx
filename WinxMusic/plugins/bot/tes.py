from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from WinxMusic import app

@app.on_message(filters.command("tes"))
async def tessss123(client, message):
    await message.reply(
    "Tes",
    reply_markup=InlineKeyboardMarkup(
       InlineKeyboardButton(
          text="Youtube",
          web_app=WebAppInfo(url="https://youtube.com")
       )
    )
    )
