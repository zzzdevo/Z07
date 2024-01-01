from pyrogram import Client, filters
from pyrogram.types import Message
from strings.filters import command
from DAXXMUSIC import app

@app.on_message(command(["groupinfo","زانیاری"]))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("**فەرمان بنووسە لەگەڵ یوزەری گرووپ یان کەناڵ\nنموونە:**\n`/ginfo , زانیاری @username`")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"**➲ هەڵە: {e}**")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # You should replace these variables with actual counts.

    response_text = (
        f"**➖➖➖➖➖➖➖\n**"
        f"**➲ ناو : {group.title} ✅\n\n**"
        f"**➲ ئایدی :** `{group.id}`\n"
        f"**➲ ئەندام : {total_members}\n**"
        f"**➲ بایۆ : {group_description or 'N/A'}\n\n**"
        f"**➲ یوزەر : @{group_username}\n**"
       
        f"➖➖➖➖➖➖➖"
    )
    
    await message.reply(response_text)






# Command handler to get group status
@app.on_message(filters.command("status") & filters.group)
def group_status(client, message):
    chat = message.chat  # Chat where the command was sent
    status_text = f"Group ID: {chat.id}\n" \
                  f"Title: {chat.title}\n" \
                  f"Type: {chat.type}\n"
                  
    if chat.username:  # Not all groups have a username
        status_text += f"Username: @{chat.username}"
    else:
        status_text += "Username: None"

    message.reply_text(status_text)


#########

""" ***                                                                       
────────────────────────────────────────────────────────────────────────
─████████████────██████████████──████████──████████──████████──████████─
─██░░░░░░░░████──██░░░░░░░░░░██──██░░░░██──██░░░░██──██░░░░██──██░░░░██─
─██░░████░░░░██──██░░██████░░██──████░░██──██░░████──████░░██──██░░████─
─██░░██──██░░██──██░░██──██░░██────██░░░░██░░░░██──────██░░░░██░░░░██───
─██░░██──██░░██──██░░██████░░██────████░░░░░░████──────████░░░░░░████───
─██░░██──██░░██──██░░░░░░░░░░██──────██░░░░░░██──────────██░░░░░░██─────
─██░░██──██░░██──██░░██████░░██────████░░░░░░████──────████░░░░░░████───
─██░░██──██░░██──██░░██──██░░██────██░░░░██░░░░██──────██░░░░██░░░░██───
─██░░████░░░░██──██░░██──██░░██──████░░██──██░░████──████░░██──██░░████─
─██░░░░░░░░████──██░░██──██░░██──██░░░░██──██░░░░██──██░░░░██──██░░░░██─
─████████████────██████──██████──████████──████████──████████──████████─
────────────────────────────────────────────────────────────────────────**"""




####

