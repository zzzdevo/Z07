from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant

app = Client(
    "subscription",
    api_id="13848352",
    api_hash="99172839e8a8d950529aebfe46528cd0",
    bot_token="YOUR_BOT_TOKEN"
)

channel = "BENfiles"
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: await app.get_chat_member(channel, user_id)
    except UserNotParticipant: return False
    return True
    
subscribed = filters.create(subscription)

@app.on_message(~subscribed)
async def checker(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]: await message.delete()
    user_id = message.from_user.id
    user = message.from_user.first_name
    markup = Markup([
        [Button("- اشتراك -", url=f"https://t.me/{channel}")]
    ])
    await message.reply(
        f"عذرًا عزيزي [{user}](tg://openmessage?user_id={user_id}) عليك الإشتراك بقناة البوت أولا.",
        reply_markup = markup
    )
    
if __name__ == "__main__": app.run()