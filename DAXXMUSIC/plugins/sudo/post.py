from pyrogram import Client, filters
from DAXXMUSIC import app
from DAXXMUSIC.misc import SUDOERS
from pyrogram.types import Message


@app.on_message(filters.command(["post"], prefixes=["/", ".", ""]) & SUDOERS)
async def copy_messages(_, message):

    if message.reply_to_message:
      
        destination_group_id = -1001906948158 

        
        await message.reply_to_message.copy(destination_group_id)
        await message.reply("𝗗𝗢𝗡𝗘✅")
