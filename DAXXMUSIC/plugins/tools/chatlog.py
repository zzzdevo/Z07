import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from DAXXMUSIC import app  

photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
    "https://graph.org/file/774380facd73524f27d26.jpg",
    "https://graph.org/file/afedfa59ab34d12c16519.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"____________________________________\n\n"
                f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"🍂 ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "**بەکارهێنەری نەناسراو**"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "**گرووپی تایبەت**"
        chat_id = message.chat.id
        left = f"**✫ لێفتی گرووپ ✫\n\nناوی گرووپ : {title}\n\nئایدی گرووپ : {chat_id}\n\nدەرکرا لەلایەن : {remove_by}\n\nبۆت : @{app.username} **"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome
@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🌷 بەخێربێی بۆ گرووپ {member.id} 🥳\n\n**"
                f"**📌 ناوی گرووپ: {message.chat.title}\n**"
                f"**🔐 یوزەری گرووپ: @{message.chat.username}\n**"
                f"**💖 ئایدی: {member.id}\n**"
                f"**✍️ یوزەر: @{member.username}\n**"
                f"**👥 ژمارەی ئەندام {count} 🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, 
            reply_markup=InlineKeyboardMarkup(
                [
                    [    
                        InlineKeyboardButton(f"⦿ زیادم بکە بۆ کەناڵت ⦿", url=f"https://t.me/IQMCBOT?startchannel=true"),
                    ],[
                        InlineKeyboardButton(text="⦿ زیادم بکە بۆ گرووپت ⦿",
                                         url=f"https://t.me/IQMCBOT?startgroup=true"),
                  ]

              ],  

           ),
        )
