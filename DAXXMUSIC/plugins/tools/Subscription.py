from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from DAXXMUSIC import app

channel = "xv7amo"
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: await app.get_chat_member(channel, user_id)
    except UserNotParticipant: return False
    return True
    
subscribed = filters.create(subscription)

@app.on_message(filters.command("play") & subscribed, group=111)
async def checker(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]: await message.delete()
    user_id = message.from_user.id
    user = message.from_user.first_name
    markup = Markup([
        [Button("♥️ جۆینی کەناڵ بکە ♥️", url=f"https://t.me/{channel}")]
    ])
    await message.reply(
        f"**🧑🏻‍💻︙ببوورە ئەزیزم تۆ جۆین نیت: [{user}](tg://openmessage?user_id={user_id})\n🔰︙سەرەتا پێویستە جۆینی کەناڵی بۆت ♥️؛\n👾︙بکەیت بۆ بەکارهێنانم جۆین بە ⚜️؛\n💎︙کەناڵی بۆت : @xv7amo\n\n👾︙کاتێ جۆینت کرد ستارت بکە /play , /vplay 📛!**",
        reply_markup = markup
    )
    
