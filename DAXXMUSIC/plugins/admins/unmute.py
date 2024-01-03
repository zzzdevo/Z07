from DAXXMUSIC import app
from pyrogram import filters,enums
from pyrogram.types import ChatPermissions 
from DAXXMUSIC.utils.daxx_ban import admin_filter

@app.on_message(filters.command(["unmuteall","لادانی میوتکراوەکان"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & admin_filter)
async def unmute_all(_,msg):
    chat_id=msg.chat.id   
    user_id=msg.from_user.id
    x = 0
    bot=await app.get_chat_member(chat_id,user_id)
    bot_permission=bot.privileges.can_restrict_members==True 
    if bot_permission:
        banned_users = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RESTRICTED):
            banned_users.append(m.user.id)       
            try:
                    await app.restrict_chat_member(chat_id,banned_users[x], ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_polls=True,can_add_web_page_previews=True,can_invite_users=True))
                    print(f"**لادانی ئاگاداری (میوت) لەسەر هەموو ئەندامەکان {m.user.mention} 🖤•**")
                    x += 1
                                        
            except Exception as e:
                print(e)
    else:
        await msg.reply_text("**من مافی ئەوەم نییە بەکارهێنەران سنووردار بکەم یان تۆ لە گەشەپێدەران نیت🖤•**")
