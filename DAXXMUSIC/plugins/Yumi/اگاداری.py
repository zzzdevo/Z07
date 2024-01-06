from pyrogram import Client, filters
from strings.filters import command
from DAXXMUSIC import app
from DAXXMUSIC.utils.daxx_ban import admin_filter

ahmed = {}
tom_max = 3

@app.on_message(command("ئاگاداربە") & admin_filter)
async def tom(client, message):
    me = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    if chat_id not in ahmed:
        ahmed[chat_id] = {}
    if user_id not in ahmed[chat_id]:
        ahmed[chat_id][user_id] = 1
    else:
        ahmed[chat_id][user_id] += 1
    await message.reply_text(f"{ahmed[chat_id][user_id]}")
    if ahmed[chat_id][user_id] >= tom_max:
        try:
        	del ahmed[chat_id][user_id]
        	await client.ban_chat_member(chat_id, user_id)
        	await message.reply("**دەرکرا♥️✅•**")   	
        except:
        	await message.reply("**نەدۆزرایەوە**")
        
