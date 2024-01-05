from pyrogram import filters
from pyrogram.types import Message
import random 
from DAXXMUSIC import app
from datetime import datetime

@app.on_message(filters.left_chat_member)
async def member_has_left(_, m: Message):
    left_gif = "https://graph.org/file/73e43b2cb7bf200bd77f1.mp4"
    await m.reply_animation(
        animation=left_gif,
        caption=f"**خوات لەگەڵ خەمباربووم بەڕۆشتنت🙂 {m.from_user.mention}\nئاگاداری خۆت بە♥!**"
    )
