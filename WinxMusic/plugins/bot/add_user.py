from pyrogram import filters
from pyrogram.types import Message
from WinxMusic import app
from WinxMusic.utils.database import add_served_chat, add_served_user


@app.on_message(filters.group & filters.command(["protecc", "spill"]))
async def play_add_user_chat(client, message):
    await add_served_chat(message.chat.id)
    await add_served_user(message.from_user.id)
