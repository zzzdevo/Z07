import os
from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from DAXXMUSIC import app


@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member)
async def WelcomeDev(_, response: ChatMemberUpdated):
    dev_id = 833360381 
    if response.from_user.id == dev_id and response.new_chat_member.status == ChatMemberStatus.MEMBER:
        info = await app.get_chat(dev_id)
        name = info.first_name
        username = info.username
        bio = info.bio
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(name, url=f"{username}.t.me")]
        ])
        await app.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
        await app.send_photo(
            chat_id=response.chat.id,
            reply_markup=markup,
            photo="downloads/developer.jpg", 
            caption=f"**• خاوەنی بۆت {name} جۆینی گرووپ بوو\n• بەخێربێی سەرۆك🧑🏻‍💻♥️\n• {bio}**"
        )
    
